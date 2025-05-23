# Aula 54 - Criando uma agenda com um banco SQLite P2

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

def query(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Operação realizada com sucesso!")
        # conexao.close()

def consultar(conexao, sql):
    c = conexao.cursor()
    c.execute(sql)
    res = c.fetchall()
    # conexao.close()

def MenuPrincipal():
    os.system('cls')
    print("Agenda PythonTerminal CFB Cursos beta v0.4 - inserir novos registros funciona!")
    print("1 - Inserir novo registro")
    print("2 - Deletar registro")
    print("3 - Atualizar registro")
    print("4 - Consultar registro por ID")
    print("5 - Consultar registro por nome")
    print("6 - Sair")

opc = 0

def MenuInserir():
    os.system('cls')
    vnome = input("Digite o nome.....: ")
    vtelefone = input("Digite o telefone..: ")
    vemail = input("Digite o email...: ")
    vsql = """INSERT INTO tb_contatos
            (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO)
            VALUES ('{}', '{}', '{}')""".format(vnome, vtelefone, vemail)
    query(vcon, vsql)

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

vcon.close()