# Aula 68 - Tkinter PhotoImage

from tkinter import *
import os

app = Tk()
app.title("CFB Cursos - Tkinter PhotoImage")
app.geometry("500x300")

pastaApp = os.path.dirname(__file__)
imgLogo = PhotoImage(file=pastaApp + '\\hqdefault2.gif')
l_logo = Label(app, image=imgLogo)
l_logo.place(x=10, y=10)
l_noticia = Label(app, text="Messi no Grêmio????? Entenda o caso", font=("Arial", 15, "italic"), fg="blue")
l_noticia.place(x=10, y=220)

os.system('cls')
app.mainloop()