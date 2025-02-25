# Aula 27 - Exercício Prático 1 P1

'''
NÃO
FUNCIONA
AINDA!!!!!!!
'''

import os 

carros = []

class Carro:
    nome = ""
    pot = 0
    velMax = 0
    ligado = False

    def __init__(self, nome, pot):
        self.nome = nome
        self.pot = pot
        self.velMax = int(pot)*2
        self.ligado = False
    
    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def info(self):
        print("Nome.........: " + self.nome)
        print("Potência.....: " + str(self.pot))
        print("Vel. Máxima..: " + str(self.velMax))
        estado = "Sim" if self.ligado == True else "Não"
        print("Ligado.......: " + estado)

def Menu():
    os.system('cls') or None
    print("1 - Novo carro")
    print("2 - Informações")
    print("3 - Excluir carro")
    print("4 - Ligar carro")
    print("5 - Desligar carro")
    print("6 - Listar carros")
    print("7 - Sair")
    print("Quantidade de carros: " + str(len(carros)))
    opc = input("Digite uma opção: ")
    return opc

def NovoCarro():
    os.system('cls') or None
    n = input("Nome do carro......: ")
    p = input("Potência do carro..: ")
    car = Carro(n, int(p))
    carros.append(car)
    print("Novo carro criado!")
    os.system("pause")

def Informacoes():
    os.system('cls') or None
    n = input("Informe o número do carro: ")
    try:
        carros[int(n)].info()
    except:
        print("Erro! Carro não existe na lista!")
        os.system("pause")

def ExcluirCarro():
    os.system('cls') or None
    n = int(input("Informe o número do carro: "))
    try:
        del carros[int(n)]
    except:
        print("Erro! Carro não existe na lista!")
        os.system("pause")

def LigarCarro():
    os.system('cls') or None
    n = int(input("Informe o número do carro que deseja ligar: "))
    try:
        carros[int(n)].ligar()
        print("Carro ligado!")
    except:
        print("Erro! Carro não existe na lista!")
        os.system("pause")

def DesligarCarro():
    os.system('cls') or None
    n = int(input("Informe o número do carro que deseja desligar: "))
    try:
        carros[int(n)].desligar()
        print("Carro desligado!")
    except:
        print("Erro! Carro não existe na lista!")
        os.system("pause")

def ListarCarros():
    os.system('cls') or None
    p = 0
    for c in carros:
        print(str(p) + " - " + c.nome)
        p += 1
    os.system("pause")
