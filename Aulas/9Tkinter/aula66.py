# Aula 65 - Tkinter frame

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
app.title("CFB Cursos - Tkinter frame")
app.geometry("500x300")
vnum_cxtexto = StringVar()
vmsg = "Curso de Python / Tkinter"

def mostrarMsg ():
        messagebox.showinfo(title="CFB Cursos", message="CFB Cursos - Curso de Python / Tkinter")

fr_quadro1 = Frame(app, borderwidth=1, relief="solid")
# Tipos de relief - solid, sunken, raised, flat, groove
fr_quadro1.place(x=10, y=10, width=300, height=120)

lb_tipo = Label(fr_quadro1, text="Tipo de caixa (1, 2, ou 3): ")
lb_tipo.place(x=10, y=10)
tb_num = Entry(fr_quadro1, textvariable=vnum_cxtexto)
vnum_cxtexto.set("1")
tb_num.place(x=13, y=40, width=130)

btn_msg = Button(fr_quadro1, text="Mostrar mensagem", command=mostrarMsg)
btn_msg.place(x=13, y=70, width=130)

fr_quadro2 = Frame(app, borderwidth=1, relief="solid", bg="#008")
# Tipos de relief - solid, sunken, raised, flat, groove
fr_quadro2.place(x=10, y=140, width=300, height=120)

lb_tipo2 = Label(fr_quadro2, text="Quadro 2!", fg="#fff", bg="#008")
lb_tipo2.place(x=10, y=10)

btn_msg = Button(fr_quadro2, text="Mostrar mensagem", command=mostrarMsg)
btn_msg.place(x=13, y=40, width=130)

os.system('cls')
app.mainloop()