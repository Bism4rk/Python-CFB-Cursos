# Aula 23 - POO: Classes

import os
os.system('cls')

# Classe: especificação de um objeto
# Objeto: instância de uma classe

class Carro:
    velMax = 0
    ligado = False
    cor = ""

c1 = Carro()
c2 = Carro()
c3 = Carro()

c1.velMax = 200
c1.ligado = False
c1.cor = "Preto"

print("Velocidade Máxima..: " + str(c1.velMax))
print("Cor................: " + c1.cor)
estado = "Sim" if c1.ligado else "Não"
print("Ligado.............: " + estado)

print('--------------------------------------------')

c2.velMax = 150
c2.ligado = False
c2.cor = "Cinza"

print("Velocidade Máxima..: " + str(c2.velMax))
print("Cor................: " + c2.cor)
estado = "Sim" if c2.ligado else "Não"
print("Ligado.............: " + estado)

c3.velMax = 250
c3.ligado = True
c3.cor = "Azul"

print('--------------------------------------------')

print("Velocidade Máxima..: " + str(c3.velMax))
print("Cor................: " + c3.cor)
estado = "Sim" if c3.ligado else "Não"
print("Ligado.............: " + estado)