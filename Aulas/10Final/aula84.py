# Aula 84 - Criando PDFs com ReportLab P2
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

def mp(mm):
    return mm / 0.352777778

pastaApp = os.path.dirname(__file__)

def criarPDF():
    try:
        cnv = canvas.Canvas(pastaApp + '\\CFBCursos.pdf', pagesize=A4)
        cnv.drawImage(pastaApp + '\\logo.jpg', mp(10), mp(207))
        cnv.drawString(mp(100), mp(232), "CFB Cursos - Criando PDFs com ReportLab")
        cnv.circle(mp(100), mp(150), mp(25), fill=0)
        cnv.drawString(mp(88), mp(150), "CFB Cursos")
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