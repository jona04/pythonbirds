class Pessoa:
    olhos = 2 #atributo de classe, ou atributo default

    def __init__(self, *filhos, nome = None, idade=33):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 33

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

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
    print(Pessoa.olhos)
    print(jonatas.olhos)
    print(silva.olhos)
    print(id(silva.olhos), id(jonatas.olhos))
    print(Pessoa.metodo_estatico(), jonatas.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe())