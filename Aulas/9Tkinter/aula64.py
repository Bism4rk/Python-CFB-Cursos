# Aula 63 - Tkinter Radio Button

from tkinter import *
import os

app = Tk()
app.title("CFB Cursos - Tkinter option menu")
app.geometry("500x300")

vesporte = StringVar()
listaEsportes = ["Futebol", "Vôlei", "Basquete"]
vesporte.set(listaEsportes[0]) # Valor padrão

def imprimirEsporte():
    ve = vesporte.get()
    if ve == "Futebol":
        print("Esporte: Futebol")
    elif ve == "Vôlei":
        print("Esporte: Vôlei")
    elif ve == "Basquete":
        print("Esporte: Basquete")
    else: 
        print("Selecione um esporte...")


bl_esportes = Label(app, text="Esportes")
bl_esportes.pack()

op_esportes = OptionMenu(app, vesporte, *listaEsportes)
op_esportes.pack()

btn_esporte = Button(app, text="Selecionar esporte", command=imprimirEsporte)
btn_esporte.pack()

os.system('cls')
app.mainloop()