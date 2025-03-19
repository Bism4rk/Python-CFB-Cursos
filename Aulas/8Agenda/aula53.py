# Aula 53 - Criando uma agenda com um banco SQLite

import os
import sqlite3
from sqlite3 import Error

def ConexaoBanco():
    caminho = "C:\\Users\\reich\\Downloads\\Python-CFB-Cursos\\Aulas\\Banco\\agenda.db"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
            print(ex)
    return con

vcon = ConexaoBanco()

def MenuPrincipal():
    os.system('cls')
    print("Agenda PythonTerminal CFB Cursos beta v0.1 - só o menu principal")
    print("1 - Inserir novo registro")
    print("2 - Deletar registro")
    print("3 - Atualizar registro")
    print("4 - Consultar registro por ID")
    print("5 - Consultar registro por nome")
    print("6 - Sair")

opc = 0

def MenuInserir():
    print("Inserir novo registro")

def MenuDeletar():
    print("Deletar registro")

def MenuAtualizar():
    print("Atualizar registro")

def MenuConsultarID():
    print("Consultar registro por ID")

def MenuConsultarNomes():
    print("Consultar registro por nome")

while opc != 6:
    try:
        MenuPrincipal()
        opc = int(input("Digite uma opção: "))
        if opc == 1:
            MenuInserir()
        elif opc == 2:
            MenuDeletar()
        elif opc == 3:
            MenuAtualizar()
        elif opc == 4:
            MenuConsultarID()
        elif opc == 5:
            MenuConsultarNomes()   
        elif opc == 6:
            print("Saindo...")
            os.system('pause')
            os.system('cls')
            print("Programa finalizado!")
        else:
            os.system('cls')
            print("Opção inválida! - Somente números de 1 a 6 são aceitos.")
            os.system('pause')    
    except ValueError:
        os.system('cls')
        print("Somente números de 1 a 6 são aceitos.")
        os.system('pause')