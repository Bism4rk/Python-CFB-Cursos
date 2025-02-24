# Aula 22 - Funções Lambda/Anônimas

import os
os.system('cls')

soma = lambda a, b: a+b
print(soma(2, 5))

mult = lambda a, b, c: (a+b)*c
print(mult(2, 5, 3))

print("-------------------------------------------")

# Criação de uma função lambda sem associá-la a uma variável

print((lambda a, b: a+b)(3, 2))

print("-------------------------------------------")

r = lambda x, func: x + func(x)

res = r(2, lambda x: x*x)
print(res) # 2 + 2*2 = 2 + 4 = 6

res = r(3, lambda x: x+x)
print(res) # 3 + 3+3 = 3 + 6 = 9

res = r(2, lambda x: x+3)
print(res) # 2 + 2+3 = 2 + 5 = 7