NORTE = 'norte'
LESTE = 'leste'
SUL = 'sul'
OESTE = 'oeste'

class Direcao:
    rotacao_direita_dic = {NORTE:LESTE, LESTE:SUL, OESTE:LESTE, LESTE:NORTE}
    rotacao_esquerda_dic = {NORTE:OESTE, OESTE:SUL, SUL:LESTE, LESTE:NORTE}

    def __init__(self):
        self.valor = 'norte';

    def girar_esquerda(self):
        self.valor = self.rotacao_esquerda_dic[self.valor]

    def girar_direita(self):
        self.valor = self.rotacao_direita_dic[self.valor]

if __name__ == '__main__':
    d = Direcao()
    print(d.valor)
    d.girar_direita()
    print(d.valor)
    d.girar_esquerda()
    print(d.valor)