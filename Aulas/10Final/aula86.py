# Aula 86 - Biblioteca URLLIB P2
import os
import urllib.request

os.system('cls')

pagina = urllib.request.urlopen('http://127.0.0.1:5500/Aulas/10Final/modelocursopython.html')
texto = pagina.read().decode('utf8')

produto = input('Digite o nome do produto: ')
produto_pos = texto.find(produto)
produto_txt = texto[produto_pos:100000]
preco_pos = produto_txt.find('R$')
preco = texto[produto_pos+preco_pos:produto_pos+preco_pos+9]


if produto_pos > -1:
    print("Produto..: " + produto)
    print("Preço....: " + preco)
else:
    print("Produto não encontrado...")
