# Aula 59 - Tkinter button

import os
import re
from tkinter import *

c = os.path.dirname(__file__)
nomeArquivo = c + "\\nomes.txt"

def gravarDados():
    arquivo = open(nomeArquivo, "a")
    arquivo.write(("Nome.........: %s" % vnome.get()))
    arquivo.write(("\nTelefone.....: %s" % vfone.get()))
    arquivo.write(("\nE-mail.......: %s" % vemail.get()))
    arquivo.write(("\nObservacoes..: %s" % vobs.get("1.0", END)))
    arquivo.write("\n\n")
    arquivo.close()


app = Tk()
app.title("CFB Cursos")
app.geometry("500x350")
app.configure(background="#dde")

Label(app, text="Nome", background="#dde", foreground="#009", anchor=W).place(x=10, y=10, width=100, height=20)

# Anchor usa os pontos cardinais em inglês --> S = South (sul), N = North (norte), E = East (leste), W = West (oeste), NE = Northeast (nordeste), SE = Southeast (sudeste), NW = Northwest (noroeste), SW = Southwest (sudoeste) -> posição do texto dentro da label

# Entry = textbox de outras línguas

vnome = Entry(app)
vnome.place(x=10, y=35, width=200, height=20)

Label(app, text="Telefone", background="#dde", foreground="#009", anchor=W).place(x=10, y=60, width=100, height=20)
vfone = Entry(app)
vfone.place(x=10, y=85, width=100, height=20)

Label(app, text="E-mail", background="#dde", foreground="#009", anchor=W).place(x=10, y=110, width=100, height=20)
vemail = Entry(app)
vemail.place(x=10, y=135, width=300, height=20)

# Text = para texto de várias linha

Label(app, text="Observações:", background="#dde", foreground="#009", anchor=W).place(x=10, y=160, width=100, height=20)
vobs = Text(app)
vobs.place(x=10, y=185, width=300, height=80)

Button(app, text="Gravar", command=gravarDados).place(x=10, y=290, width=100, height=20)

os.system('cls')
app.mainloop()