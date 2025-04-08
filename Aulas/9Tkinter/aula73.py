# Aula 73 - Tkinter LabelFrame

from tkinter import *
from tkinter import ttk
import os


app = Tk()
app.title("CFB Cursos - Tkinter LabelFrame")
app.geometry("500x300")

lb_esportes = LabelFrame(app, text="Esportes", borderwidth=1, relief="solid")
lb_esportes.place(x=10, y=10, width=300, height=100)

le1 = Label(lb_esportes, text="Futebol")
le1.pack()

le2 = Label(lb_esportes, text="Vôlei")
le2.pack()

le3 = Label(lb_esportes, text="Basquete")
le3.pack()

os.system('cls')
app.mainloop()