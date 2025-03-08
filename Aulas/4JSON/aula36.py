# Aula 36 - JSON em Python

import json
import os
os.system('cls')

carros_json='{"Marca":"Ford","Modelo":"Mustang","Cor":"Azul"}'
# Muito parecido com um dicionário

carros = json.loads(carros_json)
print(carros)
print(carros["Marca"])
print(carros["Modelo"])

# A diferença entre load e loads é que o primeiro lê de um arquivo e o segundo de uma string

print('-----------------------------------------------')

for x in carros:
    print(x + ": " + carros[x]) # Chave: valor

print("\n")

for y in carros.values():
    print(y) # Valor

print("\n")

for k, v in carros.items():
    # print(k, v)
    print(k + " - " + v) # Chave - valor

print('-----------------------------------------------')

# Convertendo dictionary para json

carros_dict = {
    "Marca": "Dodge",
    "Modelo": "Charger",
    "Cor": "Laranja"
}

carros_json2 = json.dumps(carros_dict)
print(carros_json2)

# A diferença entre dump e dumps é que o primeiro escreve em um arquivo e o segundo em uma string