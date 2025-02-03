# Aula 03 - Variáveis

# Escopo de variáveis
# Variáveis globais podem ser acessadas em qualquer parte do programa
num1=num2=num3=0
canal = "CFB Cursos"

# Variáveis locais só podem ser acessadas dentro de uma função
def cn():
    print(canal)
    curso = "Curso de Python"
    print(curso)

cn()
print(canal)
"""
print(curso) dá erro pois a variável curso é local à função cn
"""

# Se quiser declarar uma variável global dentro de uma função, use a palavra reservada global

def varglobal():
    global numglobal
    numglobal = 20
    print(numglobal)

varglobal() 
print(numglobal + num3)   