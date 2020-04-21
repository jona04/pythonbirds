class Pessoa:
    def __init__(self, *filhos, nome = None, idade=33):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    jonatas = Pessoa(nome='Jonatas')
    silva = Pessoa(jonatas,nome='Silva')
    print(silva.cumprimentar())
    print(id(silva))
    print(silva.nome)
    print(silva.idade)
    for filho in silva.filhos:
        print(filho.nome)
    jonatas.sobrenome = 'oliveira'
    del jonatas.filhos
    print(silva.__dict__)
    print(jonatas.__dict__)