# Aula 69 - Tkinter Checkbutton

from tkinter import *
import os

def futebolClicado():
    if vfutebol.get() == 1:
        print("Futebol clicado")
    else:
        print("Futebol desmarcado")

def voleiClicado():
    if vvolei.get() == 1:
        print("Vôlei clicado")
    else:
        print("Vôlei desmarcado")
    
def basqueteClicado():
    if vbasquete.get() == 1:
        print("Basquete clicado")
    else:
        print("Basquete desmarcado")

app = Tk()
app.title("CFB Cursos - Tkinter Checkbutton")
app.geometry("500x300")

vfutebol = IntVar()
vvolei = IntVar()
vbasquete = IntVar()

fr_quadro1 = Frame(app, borderwidth=1, relief="solid")
fr_quadro1.place(x=10, y=10, width=300, height=100)

cb_futebol = Checkbutton(fr_quadro1, text="Futebol", variable=vfutebol, onvalue=1, offvalue=0, command=futebolClicado)
cb_futebol.pack(side=LEFT)

cb_volei = Checkbutton(fr_quadro1, text="Vôlei", variable=vvolei, onvalue=1, offvalue=0, command=voleiClicado)
cb_volei.pack(side=LEFT)

cb_basquete = Checkbutton(fr_quadro1, text="asquete", variable=vbasquete, onvalue=1, offvalue=0, command=basqueteClicado)
cb_basquete.pack(side=LEFT)

os.system('cls')
app.mainloop()