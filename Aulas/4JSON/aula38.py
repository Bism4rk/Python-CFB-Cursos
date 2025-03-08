# Aula 38 - JSON em Python P3

import json
import os

os.system('cls')

jogador_j = '{ "Nome": "Bruno", "Time": "Aviadores", "Vivo": true, "Energia": 100, "Mochila": ["Perderneira", "Corda", "Linha", "Arame"], "Aeronaves": [{"Tipo": "Transporte","Habilidade": 80},{"Tipo": "Ataque","Habilidade": 100},{"Tipo": "Reconhecimento","Habilidade": 50}]}'

jogador = json.loads(jogador_j)

# chaves

for c in jogador:
     print(c)

print("\n")

# itens

for i in jogador.items():
     print(i)

print("\n")

# valores

for v in jogador.values():
     print(v)

print("\n")

# nome do jogador

print(jogador["Nome"])

# time do jogador

print(jogador["Time"])

print("\n")

# mochila do jogador

for im in jogador["Mochila"]:
     print(im)

print("\n")

# aeronaves do jogador

for a in jogador["Aeronaves"]:
     print(a)
     print(a["Tipo"] + " - " + str(a["Habilidade"]))
