# Aula 35 - Trabalhando com datas

import os
import datetime
os.system('cls')


data = datetime.datetime.now()
print(data)
print(str(data.day) + "/" + str(data.month) + "/" + str(data.year))

# É possível criar uma data específica

nasc = datetime.datetime(2002, 11, 18)
print(nasc)
print(nasc.strftime("%d/%m/%Y"))
print(nasc.strftime("%A"))

'''
%a - Dia da semana abreviado
%A - Dia da semana completo
%d - Dia do mês
%b - Mês abreviado
%B - Mês completo
%m - Mês (número)
%y - Ano abreviado
%Y - Ano completo
%H - Hora
%M - Minuto
%S - Segundo
%w - Dia da semana (0 = Domingo, 6 = Sábado)
%W - Semana do ano
%H - 00 a 23
%I - 00 a 12    
%p - AM ou PM
%j - Dia do ano
%f - Microsegundos
%Z - Fuso horário   
'''

print(nasc.strftime("%A, %d %B %Y"))