# Aula 70 - Tkinter Password

from tkinter import *
import os

app = Tk()
app.title("CFB Cursos - Tkinter Checkbutton")
app.geometry("500x300")
vsenha = StringVar()

def impSenha():
    senha = vsenha.get()
    print("Senha digitada: " + senha)

p_senha = Entry(app, textvariable=vsenha, show="#") # o show serve para ocultar a senha
p_senha.pack()

btn_mostraSenha = Button(app, text="Imprimir Senha", command=impSenha)
btn_mostraSenha.pack()

os.system('cls')
app.mainloop()