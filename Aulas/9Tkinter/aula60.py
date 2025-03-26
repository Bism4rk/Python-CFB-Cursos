# Aula 60 - Gravando os dados do formulário tkinter no bando de dados

import banco
import os
from tkinter import *

c = os.path.dirname(__file__)
nomeArquivo = c + "\\nomes.txt"

def gravarDados():
    if tb_nome.get() != "":
        vnome = tb_nome.get()
        vfone = tb_fone.get()
        vemail = tb_email.get()
        vobs = tb_obs.get("1.0", END)
        vquery = """INSERT INTO tb_contatos
            (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO, T_OBS)
            VALUES ('{}', '{}', '{}', '{}')""".format(vnome, vfone, vemail, vobs)
        banco.dml(vquery)
        tb_nome.delete(0, END)
        tb_fone.delete(0, END)
        tb_email.delete(0, END)
        tb_obs.delete("1.0", END)

        print("Dados gravados!")
    else:
        print("Erro! Digite um nome!")
    


app = Tk()
app.title("CFB Cursos")
app.geometry("500x350")
app.configure(background="#dde")

Label(app, text="Nome", background="#dde", foreground="#009", anchor=W).place(x=10, y=10, width=100, height=20)

# Anchor usa os pontos cardinais em inglês --> S = South (sul), N = North (norte), E = East (leste), W = West (oeste), NE = Northeast (nordeste), SE = Southeast (sudeste), NW = Northwest (noroeste), SW = Southwest (sudoeste) -> posição do texto dentro da label

# Entry = textbox de outras línguas

tb_nome = Entry(app)
tb_nome.place(x=10, y=35, width=200, height=20)

Label(app, text="Telefone", background="#dde", foreground="#009", anchor=W).place(x=10, y=60, width=100, height=20)
tb_fone = Entry(app)
tb_fone.place(x=10, y=85, width=100, height=20)

Label(app, text="E-mail", background="#dde", foreground="#009", anchor=W).place(x=10, y=110, width=100, height=20)
tb_email = Entry(app)
tb_email.place(x=10, y=135, width=300, height=20)

# Text = para texto de várias linha

Label(app, text="Observações:", background="#dde", foreground="#009", anchor=W).place(x=10, y=160, width=100, height=20)
tb_obs = Text(app)
tb_obs.place(x=10, y=185, width=300, height=80)

Button(app, text="Gravar", command=gravarDados).place(x=10, y=290, width=100, height=20)

os.system('cls')
app.mainloop()