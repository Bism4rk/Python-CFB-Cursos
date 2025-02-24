# Aula 02 - Sintaxe básica e comentários
# Variáveis no Python não precisam ter tipo definido, o tipo é definido na atribuição
num = 1
num = "Bruno"
num = 1.5

# O ; é opcional no Python, mas é possível usar para separar instruções na mesma linha
canal = "CFB Cursos"
curso = "Curso de Python"
print(canal); print(curso)
# O + é usado para concatenar strings
print(canal + " - " + curso)

# Tipos de comentários
# Comentário de uma linha
""" 
Comentário 
de várias 
linhas 
"""

# É possível inicializar várias variáveis com o mesmo valor
a = b = c = 10

# {} não é obrigtório para delimitar escopo, o que define o escopo é a identação
if 10 > 2:{
    print("10 é maior que 2")
}
    
if a == b:
    print("a é igual a b")

if 10 < 2:
    print("10 é menor que 2")
print('Fim do programa')
