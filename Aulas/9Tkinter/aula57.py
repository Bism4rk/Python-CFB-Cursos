# Aula 57 - Interface gráfica no Python com Tkinter

import os
from tkinter import *

app = Tk() # Cria a janela
app.title("CFB Cursos")
app.geometry("500x300") # Configura o tamanho da janela
app.configure(background="#008") # Muda a cor de fundo

txt1 = Label(app, text="Curso de Python", background="#008", foreground="#fff") # Configura uma label
txt1.place(x=10, y=10, width=100, height=20) # Coloca a label na janela

vtxt = "Módulo Tkinter"
vbg = "#ff0"
vfg = "#000"
txt2 = Label(app, text=vtxt, bg=vbg, fg=vfg)
txt2.pack(ipadx=20, ipady=20, padx=5, pady=5, side="top", fill=Y, expand=False)
'''
ipad = espaçamento interno
pad = espaçamento externo
fill = se expande para x (horizontal) ou y (vertical)
expand = se expande o widget pai ou não
'''

os.system('cls')
app.mainloop() # Roda a janela