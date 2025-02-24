# Aula 06 - Strings
# String é uma sequência de caracteres de texto

# Exemplo de string
curso = "Curso de Python"
print(curso)

print("------------------------------------------------------")

# O operador de indexação [] pode ser usado para acessar um caractere em uma string
print(curso[0]) # C
print(curso[9]) # P

# É possivel indexar vários caracteres de uma string
print(curso[0:5]) # Curso
print(curso[9:15]) # Python

print("------------------------------------------------------")
# Funções de string
# len() -> Retorna o comprimento da string
# strip() -> Remove espaços em branco do início e do fim da string
# lower() -> Retorna a string em minúsculas
# upper() -> Retorna a string em maiúsculas
# replace() -> Substitui uma string por outra
# split() -> Divide a string em substrings

print("Tamanho da string: " + str(len(curso))) # 14

cursoalt = "   Curso de Python   "
print(cursoalt)
print("Tamanho da string: " + str(len(cursoalt))) # 21
print(cursoalt.strip())

print (curso.lower()) # curso de python
print (curso.upper()) # CURSO DE PYTHON

print(curso.replace("Python", "C#")) # Curso de C#

a = curso.split(" ")
print(a[0]) # Curso
print(a[1]) # de
print(a[2]) # Python