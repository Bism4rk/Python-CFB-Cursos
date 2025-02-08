# Aula 08 - Booleanos
# Booleanos são um tipo de dado que pode ser True ou False (verdadeiro ou falso)

aula = True
print(aula) # True
aula2 = False
print(aula2) # True

print('---------------------------------------------------')

# Operadores de comparação em booleanos
# == (igual)
# != (difer
# > (maior)
# < (menor)
# >= (maior ou igual)
# <= (menor ou igual)

vouf = 10 < 15
print(vouf) # True

vouf2 = 10 > 15
print(vouf2) # False

print('---------------------------------------------------')

# Strings em booleanos

um = "CFB Cursos"
dois = ""
print(bool(um)) # True, pois a string não está vazia
print(bool(dois)) # False, pois a string está vazia

if(um):
    print("A string um não está vazia")
else:
    print("A string um está vazia")

if(dois):
    print("A string dois não está vazia")
else:
    print("A string dois está vazia")

print('---------------------------------------------------')

# Números em booleanos

num1 = 10
num2 = 0

print(bool(num1)) # True, pois o número é diferente de 0
print(bool(num2)) # False, pois o número é igual a 0

# De via de regra, qualquer valor nulo (ou 0) é considerado False, e qualquer valor diferente de 0 (ou não nulo) é considerado True