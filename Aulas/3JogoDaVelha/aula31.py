# Aula 31 - Jogo da Velha P2

'''
AVISO: CHECAGEM DE VITÓRIA AINDA __NÃO__ IMPLEMENTADA!
'''

import os
import random
import colorama
from colorama import Fore, Back, Style

jogarNovamente = "s"
jogadas = 0
quemJoga = 2  # 1 - CPU || 2 - Jogador
maxJogadas = 9
vit = "n"
velha = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def tela():
    global velha
    global jogadas
    os.system('cls')
    print("Jogo da velha vers. 0.3 alpha")
    print("Checagem de vitória ainda não implementada!")
    print("    0   1   2")
    print("0:  " + velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2])
    print("   -----------")
    print("1:  " + velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2])
    print("   -----------")
    print("2:  " + velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2])
    print("Jogadas: " + Fore.GREEN + str(jogadas) + Fore.RESET)

def jogadorJoga():
    global jogadas
    global quemJoga
    global maxJogadas  
    if quemJoga == 2 and jogadas < maxJogadas:
        try:
            l = int(input('Linha...: '))
            c = int(input('Coluna..: '))
            while velha[l][c] != " ":
                l = int(input('Linha...: '))
                c = int(input('Coluna..: '))
            velha[l][c] = "X"
            quemJoga = 1
            jogadas += 1
        except:
            print('Erro! Linha e/ou coluna inválida!')
            os.system('pause')
            # vit = "n"

def cpuJoga():
    global jogadas
    global quemJoga
    global maxJogadas
    if quemJoga == 1 and jogadas < maxJogadas:
        l = random.randrange(0, 3)
        c = random.randrange(0, 3)
        while velha[l][c] != " ":
            l = random.randrange(0, 3)
            c = random.randrange(0, 3)
        velha[l][c] = "O"
        quemJoga = 2
        jogadas += 1


while True:
    tela()
    jogadorJoga()
    cpuJoga()
    # checar vitória
    # break
    if jogadas == maxJogadas:
        tela()
        break
