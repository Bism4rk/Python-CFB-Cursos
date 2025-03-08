# Aula 39 - Expressões Regulares P1 (findall)

import re
import os

os.system("cls")

# findall - retorna uma lista contendo todas as ocorrências de um padrão em uma string

texto = "Curso de Python do CFB Cursos, canal do Youtube"
pesq = input("Pesquisar: ")
# res = re.findall("so", texto)
# print(res)

res = re.findall(pesq, texto)
# print(res)

qtde = len(res)

for t in res:
    print(t)

print("\n")

if len(res) == 0:
    print(pesq + " não foi encontrado!")
elif len(res) == 1:
    print(pesq + " foi encontrado 1 vez!")
else:
    print(pesq + " foi encontrado " + str(len(res)) + " vezes!")


