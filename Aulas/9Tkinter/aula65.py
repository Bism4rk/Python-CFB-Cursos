# Aula 65 - Tkinter message box

from tkinter import *
from tkinter import messagebox
import os

'''
tipos de messagebox:
show:
    showinfo
    showwarning
    showerror

ask:
    yesno (T/F)
    okcancel (T/F)
    retrycancel (T/F)
    yesnocancel (T/F/None)
'''

app = Tk()
app.title("CFB Cursos - Tkinter message box")
app.geometry("500x300")
vnum_cxtexto = StringVar()
vmsg = "Curso de Python / Tkinter"

messagebox.ask

def mostrarMsg (tipomsg, msg):
    if tipomsg == "1":
        messagebox.showinfo(title="CFB Cursos", message=msg)
    elif tipomsg == "2":
        messagebox.showwarning(title="Teste de alerta", message=msg)
    elif tipomsg == "3":
        messagebox.showerror(title="Teste de erro", message=msg)
    else:
        print("Tipo não reconhecido, tem que ser 1, 2, ou 3!")

def resetarTB():
    res=messagebox.askyesno("Resetar?", "Confirmar reset do textbox?")
    if res == True:
        tb_num.delete(0, END)
        tb_num.insert(0, "1")       

Label(app, text="Tipo de caixa (1, 2, ou 3): ").pack()
tb_num = Entry(app, textvariable=vnum_cxtexto)
vnum_cxtexto.set("1")
tb_num.pack()

btn_msg = Button(app, text="Mostrar mensagem", command=lambda:mostrarMsg(vnum_cxtexto.get(), vmsg))
btn_msg.pack()

btn_reset = Button(app, text="Resetar textbox", command=resetarTB)
btn_reset.pack()

os.system('cls')
app.mainloop()