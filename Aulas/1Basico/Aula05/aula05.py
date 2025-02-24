import random

# Aula 05 - Tipos númericos, random, e operações de casting
# Tipos númericos: int, float, complex

num_i = 10 # int (números inteiros) - 10, 20, 30, 40, 50
num_f = 5.2 # float (números decimais) - 5.2, 3.14, 2.718
num_c = 1j # complex (números complexos) - 1j, 2j, 3+2j

print("Valor: " + str(num_i) + " Tipo: " + str(type(num_i)))
print("Valor: " + str(num_f) + " Tipo: " + str(type(num_f)))
print("Valor: " + str(num_c) + " Tipo: " + str(type(num_c)))

print("-----------------------------------------------------------------------------------------------------------------------------")

# Operações de casting
# Casting é a conversão de um tipo de dado para outro
# int() -> Converte para inteiro
# float() -> Converte para decimal
# complex() -> Converte para complexo
# str() -> Converte para string

x = int(num_f) # Converte o valor de num_f para inteiro
print("Valor: " + str(x) + " Tipo: " + str(type(x))) # O tipo de X será int

y = float(num_i) # Converte o valor de num_i para decimal
print("Valor: " + str(y) + " Tipo: " + str(type(y))) # O tipo de Y será float

print("-----------------------------------------------------------------------------------------------------------------------------")

# Random
# A biblioteca random é utilizada para gerar números aleatórios
# randint() -> Gera um número inteiro aleatório
# randrange() -> Gera um número inteiro aleatório dentro de um intervalo7
# A diferença entre randint() e randrange() é que o randint() gera um número aleatório entre 2 valores, enquanto o randrange() gera um número aleatório dentro de um intervalo e não inclui o último valor


num_r = random.randrange(0, 60) # Gera um número aleatório entre 1 e 10
print("Valor: " + str(num_r) + " Tipo: " + str(type(num_r)))

num_listr = [
    random.randrange(0, 60),
    random.randrange(0, 60),
    random.randrange(0, 60),
    random.randrange(0, 60),
    random.randrange(0, 60),
    random.randrange(0, 60)
] # Gera uma lista com 6 números aleatórios entre 0 e 60
# Alternativa: random.sample(range(0, 60), 6) 
print("Valor: " + str(num_listr) + " Tipo: " + str(type(num_listr)))




