# Aula 79 - Tkinter TreeView

from tkinter import *
from tkinter import ttk
import os

app = Tk()
app.title("CFB Cursos - Tkinter TreeView")
app.geometry("500x300")

listaNomes = [['0', 'Brertilde', '9875'], ['1', 'Cristoloid', '2341'], ['2', 'Julsivam', '3784']]

tv = ttk.Treeview(app, columns=('ID', 'Nome', 'Fone'), show='headings')
tv.column('ID', minwidth=0, width=50, anchor='center')
tv.column('Nome', minwidth=0, width=250, anchor='center')
tv.column('Fone', minwidth=0, width=100, anchor='center')
tv.heading('ID', text='ID')
tv.heading('Nome', text='Nome') 
tv.heading('Fone', text='Telefone')
tv.pack()

for (id, nome, fone) in listaNomes:
    tv.insert('', 'end', values=(id, nome, fone))

os.system('cls')
app.mainloop()