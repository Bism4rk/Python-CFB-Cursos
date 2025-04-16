# Aula 83 - Tkinter TreeView P4

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import banco2

def popular():
    tv.delete(*tv.get_children())
    vquery = "SELECT * FROM tb_nomes order by id"
    linhas = banco2.dql(vquery)
    for i in linhas:
        tv.insert('', 'end', values=i)


def inserir():
    if vnome.get() == '' or vfone.get() == '':
        messagebox.showwarning('Atenção', 'Preencha todos os campos')
        return
    try:
        vquery = "INSERT INTO tb_nomes (nome, fone) VALUES ('{0}', '{1}')".format(vnome.get(), vfone.get())
        banco2.dml(vquery)
    except:
        messagebox.showwarning('Atenção', 'Erro ao inserir dados')
        return
    popular()
    vnome.delete(0, END)
    vfone.delete(0, END)
    vfone.focus()

def pesquisar():
    tv.delete(*tv.get_children())
    vquery = "SELECT * FROM tb_nomes WHERE nome LIKE '%{0}%' order by id".format(vnomepesquisar.get())
    linhas = banco2.dql(vquery)
    for i in linhas:
        tv.insert('', 'end', values=i)


app = Tk()
app.title("CFB Cursos - Tkinter TreeView")
app.geometry("600x450")

quadroGrid = LabelFrame(app, text="Contatos")
quadroGrid.pack(fill="both", expand="yes", padx=10, pady=10)

tv = ttk.Treeview(quadroGrid, columns=('ID', 'Nome', 'Fone'), show='headings')
tv.column('ID', minwidth=0, width=50, anchor='center')
tv.column('Nome', minwidth=0, width=250, anchor='center')
tv.column('Fone', minwidth=0, width=100, anchor='center')
tv.heading('ID', text='ID')
tv.heading('Nome', text='Nome') 
tv.heading('Fone', text='Telefone')
tv.pack()
popular()

quadroInserir = LabelFrame(app, text="Inserir contatos")
quadroInserir.pack(fill="both", expand="yes", padx=10, pady=10)

lb_nome = Label(quadroInserir, text="Nome") 
lb_nome.pack(side=LEFT)
vnome=Entry(quadroInserir)
vnome.pack(side=LEFT, padx=10)
lb_fone = Label(quadroInserir, text="Telefone")
lb_fone.pack(side=LEFT)
vfone=Entry(quadroInserir)
vfone.pack(side=LEFT, padx=10)

btn_inserir = Button(quadroInserir, text="Inserir", command=inserir)
btn_inserir.pack(side=LEFT, padx=10)

quadroPesquisar = LabelFrame(app, text="Pesquisar contatos")
quadroPesquisar.pack(fill="both", expand="yes", padx=10, pady=10)

lb_id = Label(quadroPesquisar, text="Nome")
lb_id.pack(side=LEFT)
vnomepesquisar=Entry(quadroPesquisar)
vnomepesquisar.pack(side=LEFT, padx=10)

btn_pesquisar = Button(quadroPesquisar, text="Pesquisar", command=pesquisar)
btn_pesquisar.pack(side=LEFT, padx=10)   

btn_todos = Button(quadroPesquisar, text="Mostrar Todos", command=popular)
btn_todos.pack(side=LEFT, padx=10)


os.system('cls')
app.mainloop()