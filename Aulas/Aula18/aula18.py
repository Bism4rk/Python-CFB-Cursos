# Aula 18 - Jogo de advinhação

import random
import os

erros = 0
sorteado = random.randrange(0, 100)
jogador = int(input("Digite seu número: "))

while(sorteado != jogador):
    os.system('cls')
    if(sorteado > jogador):
        print('Erro! Tente novamente, talvez com um número mais alto...')
    elif(sorteado < jogador):
        print('Erro! Tente novamente, talvez com um número mais baixo...')
    erros += 1
    jogador = int(input("Digite seu número: "))

print("Parabéns, o número era " + str(jogador) + "! Você acertou em " + str(erros + 1) + " tentativas!")

