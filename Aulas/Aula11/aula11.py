# Aula 11 - Condicional If, Elif, e Else

# Código da aula passada
a = 10
b = 5
op = "+" # Pode mudar o valor de op para testar as operações
res = 0

'''
if op == "+": # Dois = são utilizados para comparação
    res = a + b
    print(res)

print (str(a) +  op  + str(b) + ' = ' + str(res)) # Se op não for +, res será 0 pois a operação não foi realizada

op = "-"

if op == "-":
    res = a - b
    print(res)

print(str(a) + op + str(b) + ' = ' + str(res)) # Se op não for -, res será o resultado anterior (ou 0, se não foi executado) pois a operação não foi realizada

op = "*"

if op == "*":
    res = a * b
    print(res)


print(str(a) + op + str(b) + ' = ' + str(res)) # Se op não for *, res será o resultado anterior (ou 0, se não foi executado) pois a operação não foi realizada

op = "/"

if op == "/":
    res = a / b
    print(res)

print(str(a) + op + str(b) + ' = ' + str(res)) # Se op não for /, res será o resultado anterior (ou 0, se não foi executado) pois a operação não foi realizada
'''

# O programa acima é funcional, mas não é eficiente. O código é repetitivo e desnecessário.
# A variável op é alterada manualmente, e o código é repetido para cada operação.
# A língua python usa uma sintaxe mais eficiente para este tipo de situação: o elif.
# O elif é uma abreviação de "else if". Ele é utilizado para verificar múltiplas condições.

op = "+" # Pode mudar o valor de op para testar as operações

if op == "+":
    res = a + b
    print(res)
elif op == "-":
    res = a - b
    print(res)
elif op == "*":
    res = a * b
    print(res)
elif op == "/":
    res = a / b
    print(res)
else:
    print("Operador inválido")
print(str(a) + op + str(b) + ' = ' + str(res))

print('------------------------------------------------------')

# Operador and

clima = "sol"
lugar = ""
dinheiro = 760

if clima == "sol" and dinheiro > 300:
    lugar = "clube"
else:
    lugar = "cinema"
print("Vou ao " + lugar)

print('------------------------------------------------------')

# Parênteses podem ser utilizados para definir a ordem de execução das operações

if clima == "sol" and (dinheiro > 300 and dinheiro < 500):
    lugar = "clube"
else:
    lugar = "cinema"
print("Vou ao " + lugar)

print('------------------------------------------------------')

# Operador or

if clima == "sol" or (dinheiro > 300 and dinheiro < 500):
    lugar = "clube"
else:
    lugar = "cinema"
print("Vou ao " + lugar)

# And: retorna True se ambas as condições forem verdadeiras
# Or: retorna True se pelo menos uma das condições for verdadeira