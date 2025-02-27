# Aula 29 - Iteradores

import os 
os.system('cls')

carros = ["HRV", "Polo", "Jetta", "Cruze", "Fusion"]

# Método tradicional: for
# for c in carros:
#     print (c)

itCarros = iter(carros)
# print(next(itCarros))
# print(next(itCarros))
# print(next(itCarros))
# print(next(itCarros))
# print(next(itCarros))

print('----------------------------------------------')

# iterators em loop

while itCarros:
    try:
        print(next(itCarros))
    except StopIteration:
        print("Fim da lista!")
        break


