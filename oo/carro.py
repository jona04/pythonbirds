"""
>>> c = Carro(Motor(), Direcao())
>>> c.direcao.valor
'norte'
>>> c.calcular_velocidade()
"""

from oo.direcao import Direcao
from oo.motor import Motor


class Carro:

    def __init__(self, motor =  Motor(), direcao = Direcao()):
        self.direcao = direcao
        self.motor = motor

    def calcular_velocidade(self):
        return self.motor.velocidade

    def frear(self):
        self.motor.frear()

    def acelerar(self):
        self.motor.acelerar()

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_direita(self):
        self.direcao.girar_direita()

    def girar_esquerda(self):
        self.direcao.girar_esquerda()




if __name__ == '__main__':
    c = Carro(Motor(), Direcao())
    c2 = Carro(Motor(), Direcao())

    print(c.direcao.valor)
    print(c.calcular_velocidade())

    c.acelerar()
    print(c.calcular_velocidade())

    c.acelerar()
    print(c.calcular_velocidade())

    print(c2.calcular_velocidade())
    c2.acelerar()
    print(c2.calcular_velocidade())

    c.girar_direita()
    print(c.calcular_direcao())

    # c2.girar_direita()
    print(c2.calcular_direcao())

