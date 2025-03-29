# Aula 63 - Tkinter Radio Button

from tkinter import *
import os

app = Tk()
app.title("CFB Cursos")
app.geometry("500x300")

vesporte = StringVar()
vcor = StringVar()

def imprimirEsporte():
    ve = vesporte.get()
    if ve == "f":
        print("Esporte: Futebol")
    elif ve == "v":
        print("Esporte: Vôlei")
    elif ve == "b":
        print("Esporte: Basquete")
    else: 
        print("Selecione um esporte...")


def imprimirCor():
    vc = vcor.get()
    if vc == "#0f0":
        print("Cor: Verde")
    elif vc == "#00f":
        print("Cor: Azul")
    else: 
        print("Selecione uma cor...")


bl_esportes = Label(app, text="Esportes")
bl_esportes.pack()

rb_futebol = Radiobutton(app, text="Futebol", value="f", variable=vesporte)
rb_futebol.pack()

rb_volei = Radiobutton(app, text="Vôlei", value="v", variable=vesporte)
rb_volei.pack()

rb_basquete = Radiobutton(app, text="Basquete", value="b", variable=vesporte)
rb_basquete.pack()

btn_esporte = Button(app, text="Selecionar esporte", command=imprimirEsporte)
btn_esporte.pack()

bl_cores = Label(app, text="Cores")
bl_cores.pack()

rb_verde = Radiobutton(app, text="Azul", value="#0f0", variable=vcor)
rb_verde.pack()

rb_azul = Radiobutton(app, text="Vermelho", value="#00f", variable=vcor)
rb_azul.pack()

btn_cor = Button(app, text="Selecionar cor", command=imprimirCor)
btn_cor.pack()

os.system('cls')
app.mainloop()