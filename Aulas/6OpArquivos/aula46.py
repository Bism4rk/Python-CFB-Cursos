# Aula 46 - Operações em Arquivos P3 

import re
import os

# Cópia da aula passada
nome = "teste2.txt"
caminho = "C:/Users/reich/Downloads/Python-CFB-Cursos/Aulas/6OpArquivos/"

'''
Tente comentar um dos dois blocos de if para ver o que acontece!
'''

if os.path.exists(caminho + nome):
    print("Arquivo já existe!")
else:
    f = open(caminho + nome, "x")
    f.close()
    print("Arquivo criado!")

# Deletando arquivos
# os.remove(caminho + nome)

if os.path.exists(caminho + nome):
    os.remove(caminho + nome)
    print("Arquivo deletado!")
else:
    print("Arquivo não encontrado!")
