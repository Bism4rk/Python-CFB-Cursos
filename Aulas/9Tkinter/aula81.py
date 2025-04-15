# Aula 83 - Tkinter TreeView P3

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os

def inserir():
    if vid.get() == '' or vnome.get() == '' or vfone.get() == '':
        messagebox.showwarning('Atenção', 'Preencha todos os campos')
        return
    id = vid.get()
    nome = vnome.get()
    fone = vfone.get()
    tv.insert('', 'end', values=(id, nome, fone))
    vid.delete(0, END)
    vnome.delete(0, END)
    vfone.delete(0, END)

def deletar():
    try:
        item = tv.selection()[0]
        tv.delete(item)
    except:
        messagebox.showwarning('Atenção', 'Selecione um item para deletar')

def obter():
    try:
        item_selecionado = tv.selection()[0]
        valores = tv.item(item_selecionado, 'values')
        print("ID........: " + valores[0])
        print("Nome......: " + valores[1])
        print("Telefone..: " + valores[2])
        print('-'*50)
    except:
        messagebox.showwarning('Atenção', 'Selecione um item para obter')

app = Tk()
app.title("CFB Cursos - Tkinter TreeView")
app.geometry("500x350")

lb_id = Label(app, text="ID")
vid=Entry(app)
lb_id.grid(column=0, row=0, sticky='W', padx=1)
vid.grid(column=0, row=1, padx=5)

lb_nome = Label(app, text="Nome")
vnome=Entry(app)
lb_nome.grid(column=1, row=0, sticky='W', padx=1)
vnome.grid(column=1, row=1, padx=5)

lb_fone = Label(app, text="Telefone")
vfone=Entry(app)
lb_fone.grid(column=2, row=0, sticky='W', padx=1)
vfone.grid(column=2, row=1, padx=5)

tv = ttk.Treeview(app, columns=('ID', 'Nome', 'Fone'), show='headings')
tv.column('ID', minwidth=0, width=50, anchor='center')
tv.column('Nome', minwidth=0, width=250, anchor='center')
tv.column('Fone', minwidth=0, width=100, anchor='center')
tv.heading('ID', text='ID')
tv.heading('Nome', text='Nome') 
tv.heading('Fone', text='Telefone')
tv.grid(column=0, row=3, columnspan=3, pady=5)

btn_inserir = Button(app, text="Inserir", command=inserir)
btn_deletar = Button(app, text="Deletar", command=deletar)
btn_obter = Button(app, text="Obter", command=obter)

btn_inserir.grid(column=0, row=4)
btn_deletar.grid(column=1, row=4)
btn_obter.grid(column=2, row=4)

os.system('cls')
app.mainloop()