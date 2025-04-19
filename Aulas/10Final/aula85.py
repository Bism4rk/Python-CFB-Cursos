# Aula 85 - Biblioteca URLLIB
import os
import urllib.request

os.system('cls')

# pagina = urllib.request.urlopen('file:///C:/Users/reich/Downloads/Python-CFB-Cursos/Aulas/10Final/modelocursopython.html')
pagina = urllib.request.urlopen('http://127.0.0.1:5500/Aulas/10Final/modelocursopython.html')
texto = pagina.read().decode('utf8')
# print(texto) # Mostra o código fonte da página

dado = texto[0:15] # Mostra os 15 primeiros caracteres do código fonte
# print(dado)

# Método find
produto_pos_ini = texto.find('Mouse')
produto_pos_fim = produto_pos_ini + 5
qtde_pos_ini = produto_pos_ini + 14
qtde_pos_fim = qtde_pos_ini + 3
preco_pos_ini = qtde_pos_fim + 10
preco_pos_fim = preco_pos_ini + 7 

produto = texto[produto_pos_ini:produto_pos_fim]
qtde = texto[qtde_pos_ini:qtde_pos_fim]
preco = texto[preco_pos_ini:preco_pos_fim]

print("Produto...: " + produto)
print("Quantidade: " + qtde)
print("Preço....: " + preco)


