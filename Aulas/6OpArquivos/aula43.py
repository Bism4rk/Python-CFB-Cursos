# Aula 43 - Operações em Arquivos 

# r - read (leitura)
# w - write (escrita)
# a - append (adicionar)
# x - create (criar)
# t - text (texto)
# b - binary (binário)

f = open("C:/Users/reich/Downloads/Python-CFB-Cursos/Aulas/6OpArquivos/teste.txt", "wt") # Abre o arquivo para escrita no modo texto e o cria se não existir

f.write("CFB Cursos") # Escreve isso no arquivo
# f.write("Curso de Python") # Troca o conteúdo do arquivo, pois ele não está aberto no modo append

f.close() # Fecha o arquivo

# Modo append
f = open("C:/Users/reich/Downloads/Python-CFB-Cursos/Aulas/6OpArquivos/teste.txt", "at")

f.write("\nCurso de Python") # Adiciona isso ao final do arquivo7

f.close() # Fecha o arquivo

# Usando input no arquivo
f = open("C:/Users/reich/Downloads/Python-CFB-Cursos/Aulas/6OpArquivos/teste.txt", "at")

txt = input("Digite algo: ")

f.write("\n" + txt)

f.close()
