# Aula 52 - Consultar registros e SELECT 

import sqlite3
from sqlite3 import Error

import os

def ConexaoBanco():
    caminho = "C:\\Users\\reich\\Downloads\\Python-CFB-Cursos\\Aulas\\Banco\\agenda.db"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
            print(ex)
    return con

vcon = ConexaoBanco()

# Inserir

def inserir(conexao, sql):
     try:
          c = conexao.cursor()
          c.execute(sql)
          conexao.commit() # Confirma a inserção do registro
     except Error as ex:
        print(ex)
     finally:
          print("Registro inserido!")
          os.system('pause')
          os.system('cls')

# Deletar

def deletar(conexao, sql):
     try:
          c = conexao.cursor()
          c.execute(sql)
          conexao.commit() # Confirma a inserção do registro
     except Error as ex:
        print(ex)
     finally:
          print("Registro deletado!")
          os.system('pause')
          os.system('cls')

# Atualizar

def atualizar(conexao, sql):
     try:
          c = conexao.cursor()
          c.execute(sql)
          conexao.commit() # Confirma a inserção do registro
     except Error as ex:
        print(ex)
     finally:
          print("Registro atualizado!")
          os.system('pause')
          os.system('cls')

# Consultar

def consulta(conexao, sql):
    c = conexao.cursor()
    c.execute(sql)
    resultado = c.fetchall() # Retorna todos os registros
    return resultado
        

vsql = """SELECT * FROM tb_contatos"""
vsql2 = """SELECT * FROM tb_contatos WHERE N_IDCONTATO = 2"""
vsql3 = """SELECT * FROM tb_contatos WHERE T_NOMECONTATO LIKE '%a%'"""

res = consulta(vcon, vsql3)
for r in res:
     print(r)

os.system('pause')
os.system('cls')