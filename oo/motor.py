class Motor:

    def __init__(self, velocidade = 0):
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 1;

    def frear(self):

        if(self.velocidade > 1):
            self.velocidade -= 2;
        else:
            self.velocidade = 0

if __name__ == '__main__':
    m = Motor()

    m.acelerar()
    print(m.velocidade)

    m.acelerar()
    print(m.velocidade)

    m.acelerar()
    print(m.velocidade)

    m.frear()
    print(m.velocidade)

    m.frear()
    print(m.velocidade)