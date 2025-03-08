# Aula 39 - JSON em Python P3

import json
import os

os.system('cls')


# Importando um arquivo JSON
with open("C:/Users/reich/Downloads/Python-CFB-Cursos/Aulas/aula39.json") as f:
     jogador = json.load(f)

def linha(): print('----------------------------------------')

# chaves
for c in jogador:
     print(c)

linha()

# itens

for i in jogador.items():
     print(i)

linha()

# valores

for v in jogador.values():
     print(v)

linha()

# nome do jogador

print(jogador["Nome"])

# time do jogador

print(jogador["Time"])

linha()

# mochila do jogador

for im in jogador["Mochila"]:
     print(im)

linha()

# aeronaves do jogador

for a in jogador["Aeronaves"]:
     print(a)
     print(a["Tipo"] + " - " + str(a["Habilidade"]))
