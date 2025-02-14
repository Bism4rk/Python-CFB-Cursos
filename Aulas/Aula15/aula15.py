# Aula 15 - O que são tuplas

import os
os.system('cls')

l_carros = ['HRV', 'Golf', 'Argo']

for x in l_carros:
    print(x)

print('-------------------------------------------------')

t_carros = ('HRV', 'Golf', 'Argo')

for x in t_carros:
    print(x)


print('-------------------------------------------------')

# A diferença entre listas e tublas é que tuplas são IMUTÁVEIS enquanto listas não são

l_carros[2] = "Focus" # Muda
print(l_carros[2])

# t_carros[2] = "Focus" -> Dá erro!
print(t_carros[2])

# Métodos da tupla: index e count
print(t_carros.count('HRV'))
print(t_carros.index('Argo'))

# Lista tem muitos mais (append, clear, copy, extend, insert, pop, etc.)

print('-------------------------------------------------')

# Existe, porém, uma gambiarra para mudar índices de uma tupla

l_carros = list(t_carros)
l_carros[2] = "Focus"
t_carros = tuple(l_carros)
print(t_carros)