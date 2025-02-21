# Aula 14 - Loop While

import os
os.system('cls') # Limpa a tela do terminal antes da execução

# O loop while é um loop que executa enquanto a condição for verdadeira
# while (teste_lógico):
#     bloco de comandos

# Cuidado com loops infinitos!
# Solução: incrementar ou decrementar a variável de controle
# Exemplo: i = i + 1 ou i += 1

i = 0

while i < 9:
    print(i)
    i += 1 # Evita o loop infinito
    if(i >= 5):
        break # Encerra o loop
print("Fim do loop")

print('----------------------------------------------------------------')



carros = ['HRV', 'Golf', 'Argo', 'Onix', 'Focus']
i = 0
tam = len(carros)

while i < tam:
    print(carros[i])
    i+=1
print('\nFim do loop')

print('-----------------------------------------------------------------')

# Combinando o while com input e for

carros = []
carro = input('Digite o nome do novo carro: ')
while carro != "-1":
    carros.append(carro) # Insere o valor digitado na list carros
    carro = input('Digite o nome do novo carro: ') # Pede um novo input, que continua até o usuário digitar -1

os.system('cls')
for x in carros:
    print(x)

print('\nFim do loop')