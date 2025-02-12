# Aula 12 - Loop For

carros = ['HRV', 'Golf', 'Argo', 'Focus']

# É possível imprimir cada elemento da lista com print...
'''
print(carros[0])
print(carros[1])
print(carros[2])
print(carros[3])
'''

# ...mas é inviável fazer isso para listas muito grandes.
# Para isso, utilizamos o loop for.
# O loop for é uma estrutura de repetição que percorre todos os elementos de uma lista.

for x in carros:
    print(x)
    if (x == "Golf"):
        print('  VW')

print('----------------------------------------------------------------')

# O loop for também pode ser utilizado para percorrer strings.

for x in "CFB Cursos":
    print(x)

print('----------------------------------------------------------------')

# É possível inserir a string ou array diretamente no loop for.

for x in ["HRV", "Golf", "Argo", "Focus"]:
    print(x)

print('----------------------------------------------------------------')

carros = ['HRV', 'Golf', 'Argo', 'Focus', 'Fit', 'Fusion', 'Polo']

for x in carros:
    print(x)
    if (x == "Fit"):
        break # O comando break interrompe o loop.
    # Se o comando break estivesse antes do print, o programa não imprimiria "Fit".

print('Fim do programa')


# O for no Python funciona como o foreach em outras linguagens de programação, como o JavaScript.
