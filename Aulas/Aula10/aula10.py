# Aula 10 - Comando IF

# O comando IF é um comando de decisão, ou seja, ele permite que o programa tome decisões com base em condições.
# O comando IF é composto por uma condição e um bloco de código que será executado caso a condição seja verdadeira.
# A condição é uma expressão que retorna um valor booleano (True ou False).
# O bloco de código é um conjunto de comandos que são executados caso a condição seja verdadeira.
# O bloco de código é identificado por um recuo (tabulação) em relação ao comando IF.

# pode mudar o valor de a para True ou False para testar o código
a = False 

if a: # Condição:
    print("CFB Cursos") # Este comando será executado caso a condição seja verdadeira

print("Fim do programa") # Este comando será executado independente da condição

print('------------------------------------------------------')

# Expressões lógicas no if
a = 10
b = 5

if a > b: # Condição: a > b
    print("CFB Cursos") # Este comando será executado caso a condição seja verdadeira

if a < b: # Condição: a < b
    print("Curso de Python") # Este comando não será executado, pois a condição é falsa

print("Fim do programa") # Este comando será executado independente da condição

print('------------------------------------------------------')


op = "+" 
res = 0

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



