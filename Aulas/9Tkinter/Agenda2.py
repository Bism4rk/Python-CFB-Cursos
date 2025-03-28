# Aula 60 - Gravando os dados do formulário tkinter no bando de dados

import banco
import os
from tkinter import *

c = os.path.dirname(__file__)
nomeArquivo = c + "\\nomes.txt"

def semComando():
    print("NADA!")

def NovoContato():
    exec(open(c + "\\NovoContato.py").read(), {'x':10})

app = Tk()
app.title("CFB Cursos")
app.geometry("500x350")
app.configure(background="#dde")

barraDeMenus = Menu(app)
menuContatos = Menu(barraDeMenus, tearoff=0)
menuContatos.add_command(label="Novo", command=NovoContato)
menuContatos.add_command(label="Pesquisar", command=semComando)
menuContatos.add_command(label="Deletar", command=semComando)
menuContatos.add_separator()
menuContatos.add_command(label="Fechar", command=app.quit)
barraDeMenus.add_cascade(label="Contatos", menu=menuContatos)
app.config(menu=barraDeMenus)

menuManutencao = Menu(barraDeMenus, tearoff=0)
menuManutencao.add_command(label="Banco de Dados", command=semComando)
barraDeMenus.add_cascade(label="Manutenção", menu=menuManutencao)

menuSobre = Menu(barraDeMenus, tearoff=0)
menuSobre.add_command(label="CFB Cursos", command=semComando)
barraDeMenus.add_cascade(label="Sobre", menu=menuSobre)

os.system('cls')
app.mainloop()