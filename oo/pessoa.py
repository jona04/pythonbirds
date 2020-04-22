class Pessoa:
    olhos = 2 #atributo de classe, ou atributo default

    def __init__(self, *filhos, nome = None, idade=33):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 33

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_classe=super().cumprimentar()
        return f"{cumprimentar_classe} Aperto de mao"

class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    jonatas = Mutante(nome='Jonatas')
    silva = Homem(jonatas,nome='Silva')
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
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))

    print(isinstance(jonatas, Homem))
    print(isinstance(jonatas, Pessoa))
    print(jonatas.olhos)
    print(silva.cumprimentar())
    print(jonatas.cumprimentar())