# Aula 74 - Tkinter ListBox

from tkinter import *
from tkinter import ttk
import os

def imprimirEsportes():
    print("Esporte escolhido: " + str(lb_esportes.get(ACTIVE)))

def inserirEsporte():
    novoEsporte = vnovoesporte.get()
    listaEsportes.append(novoEsporte)
    lb_esportes.insert(END, novoEsporte)

app = Tk()
app.title("CFB Cursos - Tkinter ListBox")
app.geometry("500x300")
listaEsportes = ["Futebol", "Vôlei", "Basquete"]

lb_esportes = Listbox(app)
for esporte in listaEsportes:
    lb_esportes.insert(END, esporte)
lb_esportes.pack()

btn_esporte = Button(app, text="Imprimir Esporte", command=imprimirEsportes)
btn_esporte.pack()

vnovoesporte = Entry(app)
vnovoesporte.pack()

btn_inserirEsporte = Button(app, text="Adicionar Esporte", command=inserirEsporte)
btn_inserirEsporte.pack()


os.system('cls')
app.mainloop()