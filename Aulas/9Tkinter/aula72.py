# Aula 72 - Tkinter Scale

from tkinter import *
from tkinter import ttk
import os

def valorEscala():
    print("Valor da escala: " + str(sc_escala.get()))

app = Tk()
app.title("CFB Cursos - Tkinter Scale")
app.geometry("500x300")

lb_valor = Label(app, text="Valor")
lb_valor.pack()

sc_escala = Scale(app, from_=0, to=100, orient=HORIZONTAL) # Scale é um controle deslizante
sc_escala.set(25) # Valor padrão 
sc_escala.pack()

btn_valor = Button(app, text="Imprimir valor", command=valorEscala)
btn_valor.pack()

os.system('cls')
app.mainloop()