# Aula 71 - Tkinter ComboBox

from tkinter import *
from tkinter import ttk
import os

app = Tk()
app.title("CFB Cursos - Tkinter Checkbutton")
app.geometry("500x300")
listaEsportes = ["Futebol", "Vôlei", "Basquete"]

def imprimirEsporte():
    esporte = cb_esportes.get()
    print("Esporte escolhido: " + esporte)

lb_esportes = Label(app, text="Esportes")
lb_esportes.pack()

cb_esportes = ttk.Combobox(app, values=listaEsportes) # Combobox é uma caixa de seleção
cb_esportes.set("Futebol") # Valor padrão 
cb_esportes.pack()

btn_esporte = Button(app, text="Imprimir Esporte Escolhido", command=imprimirEsporte)
btn_esporte.pack()


os.system('cls')
app.mainloop()