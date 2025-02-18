# Aula 19 - Funções P1

# Funções são blocos de código que podem ser executadas por meio do seu nome, assim salvando espaço
# Só é necessário mudar 1 vez para mudá-la em todas

import os
os.system('cls')

n1 = 15
n2 = 7

def somar():
    r = n1+n2
    print("A soma de " + str(n1) + " e " + str(n2) + " é " + str(r))
    print("youtube.com/@cfbcursos\n")

def subtrair():
    r = n1-n2
    print(str(n1) + " menos " + str(n2) + " é igual a " + str(r))
    print("youtube.com/@cfbcursos\n")

def multiplicar():
    r = n1*n2
    print(str(n1) + " vezes " + str(n2) + " é igual a " + str(r))
    print("youtube.com/@cfbcursos\n")


# Uma função pode chamar outras funções

def calculos():
    somar()
    subtrair()
    multiplicar()

# A função deve ser chamada para ser executada

# somar()
# somar()
# subtrair()
# subtrair()

calculos()