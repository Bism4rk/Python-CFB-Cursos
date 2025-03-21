# Aula 55 - Criando uma agenda com um banco SQLite P3

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
    return res
    # conexao.close()

def MenuPrincipal():
    os.system('cls')
    print("Agenda PythonTerminal CFB Cursos beta v0.8 - deletar, atualizar adicionados!")
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
    os.system('cls')
    vid = input("Digite a ID do registro a ser deletado..: ")
    vsql = """DELETE FROM tb_contatos WHERE N_IDCONTATO = {}""".format(vid)
    query(vcon, vsql)

def MenuAtualizar():
    os.system('cls')
    vid = input("Digite a ID do registro a ser consultado..: ")
    r = consultar(vcon, "SELECT * FROM tb_contatos WHERE N_IDCONTATO = {}".format(vid))
    rnome = r[0][1]
    rtelefone = r[0][2]
    remail = r[0][3]
    vnome = input("Digite o nome.....: ")
    vtelefone = input("Digite o telefone..: ")
    vemail = input("Digite o email...: ")
    if len(vnome) == 0:
        vnome = rnome
    if len(vtelefone) == 0:
        vtelefone = rtelefone
    if len(vemail) == 0:
        vemail == remail
    vsql = """UPDATE tb_contatos SET T_NOMECONTATO = '{}', T_TELEFONECONTATO = '{}', T_EMAILCONTATO = '{}' WHERE N_IDCONTATO = {}""".format(vnome, vtelefone, vemail, vid)
    query(vcon, vsql)

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