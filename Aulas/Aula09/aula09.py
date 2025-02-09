# Aula 09 - Coleção List

# Listas são coleções de itens em Python
# Listas são ordenadas e mutáveis
# Listas são definidas por colchetes []

carros = ["HRV", "Golf", "Argo", "Focus"]
print(carros)  # ['HRV', 'Golf', 'Argo', 'Focus']
print(carros[0]) # HRV
print(carros[1]) # Golf

# É possível acessar os itens da lista de trás para frente com índices 

print('------------------------------------------------------------')

print(carros[-1]) # Focus
print(carros[-2]) # Argo

print('------------------------------------------------------------')

# É possível mudar o valor de um item da lista
carros[3] = "Fusion"
print(carros) # ['HRV', 'Golf', 'Argo', 'Fusion']

print('------------------------------------------------------------')


# Adicionar um item à lista
carros.append("Fit")
carros.append("Polo")
carros.append("Civic")
print(carros) # ['HRV', 'Golf', 'Argo', 'Fusion', 'Fit', 'Polo', 'Civic']

print('------------------------------------------------------------')

# Obtendo o tamanho da lista
print(str(len(carros)) + " carros na lista") # 6 carros na lista


print('------------------------------------------------------------')

# Removendo um item da lista
carros.remove("Fusion")
print(carros) # ['HRV', 'Golf', 'Argo', 'Fit', 'Polo', 'Civic'] 

# carros.remove('Palio') Erro, pois o item não existe na lista

print('------------------------------------------------------------')

# Removendo um item da lista com pop
carros.pop() # Remove o último item da lista (Civic)
print(carros) # ['HRV', 'Golf', 'Argo', 'Fit', 'Polo']

print('------------------------------------------------------------')

# Removendo um item da lista com del

del carros[2] # Remove o item no índice 2 (Argo)
print(carros) # ['HRV', 'Golf', 'Fit', 'Polo']

print('------------------------------------------------------------')

# Limpar a lista
'''
carros.clear()
print(carros) # []
'''

print('------------------------------------------------------------')

# Junção de listas

carros2 = ["Fusca", "147", "Brasília", "Opala"]
carros3 = carros + carros2
print(carros3) # ['HRV', 'Golf', 'Fit', 'Polo', 'Fusca', '147', 'Brasília', 'Opala']
print(str(len(carros3)) + " carros na lista") # 8 carros na lista