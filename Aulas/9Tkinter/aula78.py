# Aula 78 - Tkinter Grid

from tkinter import *
from tkinter import ttk
import os

app = Tk()
app.title("CFB Cursos - Tkinter Grid")
app.geometry("500x300")

lb_canal = Label(app, text="CFB Cursos")
lb_nome = Label(app, text="Digite seu nome")
lb_idade = Label(app, text="Digite sua idade")

et_nome = Entry(app)
et_idade = Entry(app)

btn = Button(app, text="Enviar")

lb_canal.grid(row=0, column=0, columnspan=2, pady=15) # O columnspan=2 faz o texto ocupar duas colunas
lb_nome.grid(row=1, column=0, sticky=W) # O sticky=W faz o texto ficar alinhado a esquerda
et_nome.grid(row=2, column=0, sticky=W, padx=5) # o padx=5 adiciona um espaço de 5 pixels a esquerda do campo de texto
lb_idade.grid(row=1, column=1, sticky=W)
et_idade.grid(row=2, column=1, sticky=W, padx=5)

os.system('cls')
app.mainloop()