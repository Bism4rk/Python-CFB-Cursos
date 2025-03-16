# Aula 50 - Deletando registros na tabela e DELETE

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

vsql = """DELETE FROM 
            tb_contatos
            WHERE N_IDCONTATO = 5"""

# inserir(vcon, vsql)

deletar(vcon, vsql)
