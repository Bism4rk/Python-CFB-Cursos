# Aula 51 - Atualizando registros na tabela e UPDATE

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

vsql = """UPDATE tb_contatos SET T_NOMECONTATO = 'Joanéllison Paulo Catarinense', T_TELEFONECONTATO = '(31)23586-7861', T_EMAILCONTATO = 'joanelisonpaulosc@futmail.com' WHERE N_IDCONTATO = 2"""

atualizar(vcon, vsql)