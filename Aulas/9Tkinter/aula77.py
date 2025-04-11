# Aula 77 - Tkinter ProgressBar

from tkinter import *
from tkinter import ttk
import os

def valBarra():
    if varBarra.get() < 100:
        varBarra.set(varBarra.get() + 10)
    else:
        varBarra.set(0)

def valBarraCont(m):
    cont = 0
    etapas = m/100

    while cont < etapas:
        cont = cont + 1
        i = 0
        while i < 1000000:
            i = i + 1
        varBarra.set(cont)
        app.update()

def resetarBarra():
    varBarra.set(0)


app = Tk()
app.title("CFB Cursos - Tkinter ProgressBar")
app.geometry("500x300")

varBarra = DoubleVar()
varBarra.set(0)

pb = ttk.Progressbar(app, variable=varBarra, maximum=100)
pb.place(x=10, y=10, width=200, height=30)

btn = Button(app, text="Avançar", command=valBarra)
btn.place(x=10, y=50, width=100, height=30)

btn2 = Button(app, text="Preencher barra", command=lambda: valBarraCont(10000))
btn2.place(x=10, y=90, width=100, height=30)

btn3 = Button(app, text="Resetar barra", command=resetarBarra)
btn3.place(x=10, y=130, width=100, height=30)


os.system('cls')
app.mainloop()