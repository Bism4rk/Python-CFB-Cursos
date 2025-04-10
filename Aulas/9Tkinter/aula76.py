# Aula 76 - Tkinter abas e notlook

from tkinter import *
from tkinter import ttk
import os

app = Tk()
app.title("CFB Cursos - Tkinter Abas e Notebook")
app.geometry("500x300")

nb = ttk.Notebook(app)
nb.place(x=0, y=0, width=500, height=300)

tb1 = Frame(nb)
nb.add(tb1, text="Cursos")

tb2 = Frame(nb)
nb.add(tb2, text="Canal")

lb1 = Label(tb1, text="Curso de Python", font=("Arial", 13))
lb1.pack()

lb2 = Label(tb1, text="Curso de ReactNative", font=("Arial", 13))
lb2.pack()

lb3 = Label(tb2, text="youtube.com/@cfbcursos", font=("Arial", 13))
lb3.pack()


os.system('cls')
app.mainloop()