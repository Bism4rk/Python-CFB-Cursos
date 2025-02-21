# Aula 19 - Funções P2, Parâmetros de Entrada

import os
os.system('cls')

'''
Código da aula passada
n1 = 15
n2 = 7

def somar():
    r = n1+n2
    print("A soma de " + str(n1) + " e " + str(n2) + " é " + str(r))
    print("youtube.com/@cfbcursos\n")

somar()
'''

# Inserindo parâmetros de entrada

def somar(n1, n2, n3, n4):
    r = n1+n2+n3+n4
    print("A soma de " + str(n1) + ", " + str(n2) + ", " + str(n3) + " e " + str(n4) +  " é " + str(r))
    print("youtube.com/@cfbcursos\n")

# Os valores do parâmetros devem ser inseridos na chamada da função

somar(5, 7, 3, 2)
somar(12, 8, 1, 20)
somar(1, 2, 0, 0)

print('----------------------------------------------------------------')

# Argumentos arbritrários

def textos(*txt):
    for t in txt:
        print(t)

textos("Python", "Canal", "Curso", "Computador", "Funções")

def somar2(*num):
    r = 0
    for n in num:
        r += n
    print("Soma = " + str(r))

somar2(5, 2)
somar2(5, 2, 3)
somar2(5, 2, 3, 5, 20, 15, 0, 1, 37)

print('----------------------------------------------------------------')

# Valor padrão de argumento

def carros(c = "Golf"):
    print("Modelo: " + c)

carros()

print('----------------------------------------------------------------')

# Usando lists como parâmetros

valores = [1, 5, 3, 2]

def somar3(num):
    r = 0
    for n in num:
        r += n
    print("Soma = " + str(r))

somar3(valores)