# Aula 13 - Função Input

import os
os.system('cls')


nome = input("Digite seu nome: ") # Função input() recebe um valor digitado pelo usuário
print("Nome digitado: " + nome) # Imprime o valor digitado pelo usuário

print('----------------------------------------------------------------')

# Soma de dois números digitados pelo usuário
num1 = int(input("Digite o primeiro valor..: ")) # Função input() recebe um valor digitado pelo usuário
num2 = int(input("Digite o segundo valor...: ")) # Função input() recebe um valor digitado pelo usuário
soma = num1 + num2
print("A soma de " + str(num1) + " e " + str(num2) + " é " + str(soma) + "!") # Imprime o valor digitado pelo 

# Importante: é necessário converter os valores digitados para inteiros, pois a função input() retorna uma string