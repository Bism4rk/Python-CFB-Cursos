# Aula 49 - Inserindo registros na tabela e INSERT INTO

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

nome = input("Digite o nome..........: ")
telefone = input("Digite o telefone..: ")
email = input("Digite o email........: ")

vsql = """INSERT INTO tb_contatos
            (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO)
            VALUES ('{}', '{}', '{}')""".format(nome, telefone, email)

 
  
def inserir(conexao, sql):
     try:
          c = conexao.cursor()
          c.execute(sql)
          conexao.commit() # Confirma a inserção do registro
          print("Registro inserido!")
          os.system('pause')
          os.system('cls')
     except Error as ex:
        print(ex)

inserir(vcon, vsql)