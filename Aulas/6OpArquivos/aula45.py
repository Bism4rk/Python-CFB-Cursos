# Aula 45 - Operações em Arquivos P2

import re

# Modo read (leitura)
f = open("C:/Users/reich/Downloads/Python-CFB-Cursos/Aulas/6OpArquivos/teste.txt", "rt") # Abre o arquivo para leitura no modo texto

# print(f.read()) # Lê o conteúdo do arquivo
# print(f.read(10)) # Lê os 10 primeiros caracteres do 
# print(f.readline()) # Lê a primeira linha do arquivo
# print(f.readline()) # Lê a segunda linha do arquivo
'''
for l in f: # Loop para ler todas as linhas do arquivo
    l = l.strip() # Remove os espaços em brando e quebras de linha
    print(l)
'''

res = re.sub("\\s", "-", f.readline()) # duas barras para não ser interpretado como caractere de escape
print(res)
f.close()

f = open("C:/Users/reich/Downloads/Python-CFB-Cursos/Aulas/6OpArquivos/teste.txt", "wt")
f.write(res)
f.close()