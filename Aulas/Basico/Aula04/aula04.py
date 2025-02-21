# Aula 04 - Tipos de Dados

x = 1
print("Valor: " + str(x)) # O str() converte o valor para string
print("Tipo: " + str(type(x))) # int (inteiro) -> Números inteiros

print("-----------------------------------------------------------------------------------------------------------------------------")

y = "CFB Cursos"
print("Valor: " + y)
print("Tipo: " + str(type(y))) # str (string) -> Texto

print("-----------------------------------------------------------------------------------------------------------------------------")

z = 15.6
print("Valor: " + str(z))
print("Tipo: " + str(type(z))) # float (flutuante) -> Números decimais

print("-----------------------------------------------------------------------------------------------------------------------------")

a = True # Booleano no Python SEMPRE começa com letra maiúscula
print("Valor: " + str(a))
print("Tipo: " + str(type(a))) # bool (booleano) -> True ou False (Verdadeiro ou Falso)

print("-----------------------------------------------------------------------------------------------------------------------------")

n1 = 5; n2 = 2; b = complex(n1, n2)
print("Valor: " + str(b))
print("Tipo: " + str(type(b))) # complex (complexo) -> Números complexos (n1 é a parte real e n2 é a parte imaginária)
print("Parte real: " + str(b.real)) # Acessando a parte real do número complexo
print("Parte imaginária: " + str(b.imag)) # Acessando a parte imaginária do número complexo

print("-----------------------------------------------------------------------------------------------------------------------------")

# Coleções
# Coleções são estruturas que permitem armazenar vários valores em uma única variável

c = ["Carro", "Avião", "Navio", "Ônibus", "Trem"] 
print("Valor: " + str(c))
print("Tipo: " + str(type(c))) # Lista (list) -> Coleção de valores ordenados (como o array do JavaScript)
print(c[0]) # Acessando o primeiro elemento da lista
c[0] = "Ônibus" # Alterando o valor do primeiro elemento da lista
print(c[0]) # Acessando o primeiro elemento da lista que foi alterado
# Lists podem conter valores de tipos diferentes (ex: y =[1, "CFB Cursos", 15.6, True])

print("-----------------------------------------------------------------------------------------------------------------------------")

# Tupla
# A tupla é uma coleção de valores ordenados e imutável (não pode ser alterada)
# A tupla também aceita valores de tipos diferentes

d = ("Carro", "Avião", "Navio", "Ônibus", "Trem")
''' d[0] = "Ônibus" # Isso gerará um erro, pois a tupla é imutável '''
print("Valor: " + str(d))
print("Tipo: " + str(type(d)))

print("-----------------------------------------------------------------------------------------------------------------------------")

e = range(0, 100, 1) # range() -> Gera uma sequência de números
print("Valor: " + str(e))
print("Tipo: " + str(type(e))) # range -> Sequência de números

print("-----------------------------------------------------------------------------------------------------------------------------")

# Dictinonary (Dicionário)
# O dicionário é uma coleção de valores não ordenados, mutáveis e indexados

f = {
    "canal": "CFB Cursos",
    "curso": "Curso de Python",
    "nome": "Bruno"
}

print("Valor: " + f["canal"]) # Acessando o valor do dicionário pela chave
print("Valor: " + f["curso"]) # Acessando o valor do dicionário pela chave
print("Valor: " + f["nome"]) # Acessando o valor do dicionário pela chave
print("Tipo: " + str(type(f))) # dict (dicionário) 

print("-----------------------------------------------------------------------------------------------------------------------------")

# Set (Conjunto)
# O set é uma coleção de valores não ordenados e sem elementos duplicados na chamada

g = {5,7,4,5,7,4,8}
print("Valor: " + str(g)) # Note que os valores duplicados não são exibidos
print("Tipo: " + str(type(g))) # set (conjunto)

h = frozenset({5,7,4,5,7,4,8}) # O frozenset() cria um conjunto imutável
print ("Valor: " + str(h))
print("Tipo: " + str(type(h))) # frozenset (conjunto imutável)
'''
h[0] = 10 # Isso gerará um erro, pois o conjunto é imutável
'''