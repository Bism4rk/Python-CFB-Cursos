# Aula 47 - SQLite, banco de dados, e tabelas

import os
os.system('cls')


libraries = 'Libraries usadas em Python para trabalhar com SQLite: \nimport sqlite3, \nfrom sqlite3 import Error'
codigousado = 'CREATE TABLE tb_contatos (N_IDCONTATO INTEGER PRIMARY KEY AUTOINCREMENT, T_NOMECONTATO TEXT (30 T_TELEFONECONTATO TEXT (14),  T_EMAILCONTATO TEXT (30));'

print(libraries)
print("\n")
print('Código usado na aula no SQLiteStudio: \n' + codigousado)