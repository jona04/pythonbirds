class Pessoa:
    def __init__(self, nome = None, idade=33):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Silva')
    print(p.cumprimentar())
    print(id(p))
    print(p.nome)
    p.nome = "Jonatas"
    print(p.nome)
    print(p.idade)
