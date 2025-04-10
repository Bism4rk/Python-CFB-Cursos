# Aula 75 - Tkinter SpinBox

from tkinter import *
from tkinter import ttk
import os

def ImpVal1():
    print("Valor 1: " + str(sb_valores.get()))

def ImpVal2():
    print("Valor 2: " + str(sb_valores2.get()))

app = Tk()
app.title("CFB Cursos - Tkinter SpinBox")
app.geometry("500x300")

lb_spinbox = LabelFrame(app, text="Spinbox", borderwidth=1, relief="solid")
lb_spinbox.place(x=10, y=10, width=480, height=150)

sb_valores = Spinbox(lb_spinbox, from_=0, to=100)
sb_valores.place(x=150, y=10)

sb_valores2 = Spinbox(lb_spinbox, values=(1, 2, 3, 4, 5))
sb_valores2.place(x=150, y=40)

btn_valor = Button(lb_spinbox, text="Imprimir Valor 1", command=ImpVal1)
btn_valor.place(x=150, y=70, width=135)

btn_valor2 = Button(lb_spinbox, text="Imprimir Valor 2", command=ImpVal2)
btn_valor2.place(x=150, y=100, width=135)

os.system('cls')
app.mainloop()