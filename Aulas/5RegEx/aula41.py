# Aula 41 - Expressões Regulares P2 (search)

import re
import os

os.system("cls")

# Search - retorna um objeto Match (a primeira ocorrência encontrada) se encontrar um padrão em uma string

texto = "Curso de Python do CFB Cursos, canal do Youtube"
res = re.search("canal", texto)
print(res)

if res == None:
    print("Não encontrado!")
else:
    pi = res.start()
    pf = res.end()
    tam = pf - pi
    print("Posição inicial..: " + str(pi))
    print("Posição final....: " + str(pf))
    print("Tamanho..........: " + str(tam))