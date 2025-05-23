# Aula 83 - Criando PDFs com ReportLab
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

pastaApp = os.path.dirname(__file__)

def criarPDF():
    try:
        cnv = canvas.Canvas(pastaApp + '\\CFBCursos.pdf', pagesize=A4)
        cnv.drawString(10, 800, "CFB Cursos - Criando PDFs com ReportLab")
        cnv.drawString(10, 780, "Curso de Python")
        cnv.circle(100, 700, 50, stroke=1, fill=0)

        cnv.save()
    except:
        messagebox.showwarning('Atenção', 'Erro ao criar PDF')
        return
    messagebox.showinfo('Sucesso!', 'PDF criado com sucesso!')

app = Tk()
app.title("CFB Cursos - Criando PDFs com ReportLab")
app.geometry("400x80")

lb_criar = Label(app, text="Criar PDF", anchor="center")
lb_criar.pack(pady=10)
btn_criarPDF = Button(app, text="Criar PDF", command=criarPDF, anchor="center")
btn_criarPDF.pack()

os.system('cls')
app.mainloop()