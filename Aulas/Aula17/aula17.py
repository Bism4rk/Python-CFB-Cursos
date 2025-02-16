# Aula 17 - Dictionary
# Coleção aberta, como as lists

import os
os.system('cls')

carro = {
    # chave (key): valor
    "Fabricante": "Honda",
    "Modelo": "HRV",
    "Ano": "2016",
    "Cor": "Prata"
}

print(carro)
print(carro["Modelo"])
fab = carro["Fabricante"] # carro.get("Fabricante") funciona igual
print(fab)

carro["Cor"] = "Preto"
print(carro["Cor"])

print('----------------------------------------------------------------------------------')

'''
Alternativa 1
for x in carro:
    # print(x) Imprime as chaves
    print(x + ": " + carro[x])
'''

# Alternativa 2
for c,v in carro.items():
    print(c + ": " + v)

print('----------------------------------------------------------------------------------')

if "Modelo" in carro:
    print("SIM, modelo é uma chave! \n")

print("Tamanho do dictionary: " + str(len(carro)))

print('----------------------------------------------------------------------------------')

carro["Câmbio"] = "Automático"

for c,v in carro.items():
    print(c + ": " + v)

print("\n")

carro.pop("Câmbio") # ou del carro("Câmbio")

# carro.clear() Limpa tudo

for c,v in carro.items():
    print(c + ": " + v)

print('----------------------------------------------------------------------------------')

'''
carros = {
    "Carro1":{
        "Fabricante": "Honda",
        "Modelo": "HRV"
    },
    "Carro2":{
        "Fabricante": "Volkswagen",
        "Modelo": "Golf"
    },
    "Carro3":{
        "Fabricante": "Ford",
        "Modelo": "Focus"
    }
}

print(carros["Carro1"])
print(carros["Carro1"]["Fabricante"])
'''

Carro1 = {
        "Fabricante": "Fiat",
        "Modelo": "147"
    }

Carro2 = {
    "Fabricante": "Volkswagen",
    "Modelo": "Brasília"
}
Carro3 = {
    "Fabricante": "Chevrolet",
    "Modelo": "Opala"
}

carros = {
    "C1": Carro1,
    "C2": Carro2,
    "C3": Carro3
}

print(carros["C1"])