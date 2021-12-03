from datetime import datetime


class Pessoa:
    ano_atual = datetime.today().year

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade= idade
        self.comendo = comendo
        self.falando = falando

    @classmethod  # ← indicado de método de classe
    def por_ano_nascimento(cls, nome, ano_nascimento):  # método de classe, não de instância.
        # 'cls' é usado por convenção.
        idade = cls.ano_atual - ano_nascimento
        # ↑ variável interna ao método de classe
        return Pessoa(nome, idade)
    # como esse método é um construtor da classe, pode-se chamar de "factory method"


if __name__ == '__main__':
    pessoa_1 = Pessoa.por_ano_nascimento('João', 1988)
    # ↑ invocando o método para a criação de uma intância
    print(pessoa_1.nome)
    print(pessoa_1.idade)
    pessoa_2 = Pessoa.por_ano_nascimento('Zeca', 1975)
    print(pessoa_2.nome)
    print(pessoa_2.idade)
