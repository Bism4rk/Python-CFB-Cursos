# Aula 43 - Expressões Regulares P4 (sub)

import re
import os
os.system("cls")

# search - substitui parte de uma string que corresponde a um padrão por outra

texto = "Curso de Python do CFB Cursos, canal do Youtube"  

res = re.sub("Python", "SQL", texto) # Substitui a palavra Python por SQL
res = re.sub("\s", "-", texto) # Substitui os espaços por hífen
res = re.sub(",", "-", res) # Substitui a vírgula por 

print(texto)
print(res)
 
print('-'*80) # Imprime um hífen 80 vezes

texto2 = "Curso de Python no Youtube - Curso feito pelo CFB Cursos"
res2 = re.sub("-", ",", texto2)
res2 = re.sub("Curso", "curso", res2)

print(texto2)
print(res2)