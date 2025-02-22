# Aula 24 - Classes P2: Construtor e métodos

import os
os.system('cls')

# Construtor - função chamada quando um novo objeto é instanciado
class Carro:
    velMax = 0
    ligado = False
    cor = ""
    def __init__(self, v, l, c): # self: equivalente ao this de outras línguas
        self.velMax = v
        self.ligado = l
        self.cor = c
    def ligar(self):
        self.ligado = True
    def desligar(self):
        self.ligado = False
    def andar(self):
        if(self.ligado):
            print("Carro andando!")
        else:
            print("O carro está desligado!")
    def mostrar(self):
        print("Velocidade Máxima..: " + str(self.velMax))
        print("Cor................: " + self.cor)
        estado = "Sim" if self.ligado else "Não"
        print("Ligado.............: " + estado)
        print('------------------------------------')


c1 = Carro(200, False, "Preto")
c2 = Carro(150, False, "Branco")
c3 = Carro(350, True, "Azul")

c1.mostrar()
c2.mostrar()
c3.mostrar()

c1.ligar()
c3.desligar()

c1.andar()
c2.andar()
c3.andar()
