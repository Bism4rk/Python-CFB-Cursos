# Aula 36 - JSON em Python P2

import json
import os
os.system('cls')

carros_dictionary = {
    "Marca": "Ford",
    "Modelo": "Mustang",
    "Cor": "Azul"
}
# dictionary -> objeto json

carros_lista = ["Honda", "Volkswagen", "Ford", "Fiat", "Chevrolet"]
# list -> array json

carros_tupla = ("Honda", "Volkswagen", "Ford", "Fiat", "Chevrolet")
# tupla -> array 

carros_j = json.dumps(carros_dictionary)
print(carros_j)

carros_j2 = json.dumps(carros_lista) 
print(carros_j2)

carros_j3 = json.dumps(carros_tupla)
print(carros_j3)

carros_j = json.dumps(carros_dictionary, indent = 4, separators=(": ", " = "), sort_keys = True)
print(carros_j)

# Indent = gera indentação
# Separators = muda o separador padrão (:)
# Sort_keys = ordena as chaves

jogador_j = '{ "Nome": "Bruno", "Time": "Aviadores", "Vivo": true, "Energia": 100, "Mochila": ["Perderneira", "Corda", "Linha", "Arame"], "Aeronaves": [{"Tipo": "Transporte","Habilidade": 80},{"Tipo": "Ataque","Habilidade": 100},{"Tipo": "Reconhecimento","Habilidade": 50}]}'


# jogador_j2='{"nome": "Bruno","time": "aviadores","vivo": "True","energia": 100,"mochila": ["pederneira", "corda", "linha", "arame"],"aeronaves": [{"tipo": "transporte", "habilidade": 80},{"tipo": "ataque", "habilidade": 100},{"tipo": "reconhecimento", "habilidade": 50}]}'

jogador = json.loads(jogador_j)
jogador_j2 = json.dumps(jogador, indent = 4, separators=(": ", " = "))
print(jogador_j2)