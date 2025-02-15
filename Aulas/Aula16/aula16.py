# Aula 16 - Matrizes
# Trabalha com 2 índices - linha *e coluna*

import os
os.system('cls')

# List -> array comum

carros = ["HRV", "Golf", "Focus", "Argo"]

for x in carros:
    print(x)

carros[2] = "Fusion"
print(carros[2])

print('------------------------------------------------------------')

carros_m = [
    ["Modelo","HRV"], # Linha 0
    ["Fabricante","Honda"], # Linha 1
    ["Ano",2016] # Linha 2
    ]

  
print(carros_m[0][0])
print(carros_m[0][1])
print(carros_m[1][1])
print(carros_m[2][0])


for l, c in carros_m:
    print("Linha: " + l + " | Coluna: " + str(c))

carros_m[2][1] = 2019
carros_m.append(["Cor", "Prata"])

print("\n")

for l, c in carros_m:
    print(l + " | " + str(c))



