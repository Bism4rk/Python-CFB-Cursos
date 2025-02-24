# Aula 26 - Tratamento de erros

import os
os.system('cls')
 
# Try/except/finally

x = 10

try:
    print(x)
except NameError:
    print("Erro! Variável não definida!")
except:
    print("Erro no programa!")
else:
    print("Tudo certo!")
finally:
    print("Fim do tratamento")

print('---------------------------------------------')

# raise Exception

num = -10
'''
if num < 1:
    raise Exception("Valor não permitido!")
'''
# num = "Bruno"

if not type(num) is int:
    raise Exception("Somente números permitidos!")
else:
    print(num)