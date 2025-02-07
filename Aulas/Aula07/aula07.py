# Aula 07 - Strings parte 2

curso = "Curso de Python"

# (not) in
# Verifica se uma string está contida (ou se não está) em outra
# Retorna True ou False

res_in = print("Python" in curso) # True
res_notin = print("Python" not in curso) # False

print('---------------------------------------------')

# É case sensitive

res_in = print("python" in curso) # False

print('---------------------------------------------')


# variáveis em in

texto = "Curso de Python"
palavra = "Python"

res = print(palavra in texto) # True
res_upper = print(palavra.upper() in texto.upper()) # True
res_upper = print(palavra.upper() not in texto.upper()) # False


print('---------------------------------------------')

# Concatenação de strings
# O + é usado para concatenar strings

canal = "CFB Cursos"

res = curso + " - " + canal
print(res) # Curso de Python - CFB Cursos

res = curso + " do canal " + canal
print(res) # Curso de Python do canal CFB Cursos

print('---------------------------------------------')

# Concatenação de strings e números

cidade = "Porto Alegre"
dia = 7
mes = "fevereiro"
ano = 2025
data = cidade + ", " + str(dia) + " de " + mes + " de " + str(ano)
print(data) # 7 de Fevereiro de 2025

# string.format()

data = "{}, {} de {} de {}".format(cidade, dia, mes, ano)
print(data) # Porto Alegre, 7 de fevereiro de 2025

print('---------------------------------------------')

# caracteres de escape
# \n - nova linha
# \" - aspas duplas
# \' - aspas simples
# \r - retorno de carro (enter)
# \t - tabulação (tab)
# \b - backspace

data = "{}, {} de {} de {} \n{}".format(cidade, dia, mes, ano, canal)
print(data) # Porto Alegre, 7 de fevereiro de 2025 (nova linha) CFB Cursos

data = "{}, {} de {} de {} \"{}\"".format(cidade, dia, mes, ano, canal)
print(data) # Porto Alegre, 7 de fevereiro de 2025 "CFB Cursos"