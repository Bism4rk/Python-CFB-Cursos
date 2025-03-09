# Aula 41 - Expressões Regulares P3 (split)

import re 
import os
os.system("cls")

texto = "Curso de Python do CFB Cursos, canal do Youtube"  

res = re.split(" ", texto)
print(res)
print(res[2])

print('----------------')

# for t in res:
#     print(t)

res2 = re.split(", ", texto)
print(res2)
print(res2[1])