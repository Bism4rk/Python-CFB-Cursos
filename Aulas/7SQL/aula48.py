# Aula 48 - Criando conexão com o banco de dados e criando tabelas

import sqlite3
from sqlite3 import Error

# Criando a conexão com o banco de dados

def ConexaoBanco():
    caminho = "C:\\Users\\reich\\Downloads\\Python-CFB-Cursos\\Aulas\\Banco\\agenda.db"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
            print(ex)
    return con

vcon = ConexaoBanco()

# Criando tabela

vsql = """CREATE TABLE tb_contatos (
            N_IDCONTATO INTEGER PRIMARY KEY AUTOINCREMENT, 
            T_NOMECONTATO TEXT (30), 
            T_TELEFONECONTATO TEXT (14),  
            T_EMAILCONTATO TEXT (30))""" # Aspas triplas para quebra de linha

def CriarTabela(conexao, sql):
     try:
          c = conexao.cursor() # Cursor é um objeto que permite interagir com o banco de dados
          c.execute(sql)
          print("Tabela criada!")
     except Error as ex:
        print(ex)

CriarTabela(vcon, vsql)

vcon.close() # Fechando a conexão com o banco de dados 