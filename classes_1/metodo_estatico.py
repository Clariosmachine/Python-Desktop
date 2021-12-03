from datetime import datetime


class Pessoa:
    ano_atual = datetime.today().year

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade= idade
        self.comendo = comendo
        self.falando = falando

    @classmethod  # ← indicador de método de classe
    def por_ano_nascimento(cls, nome, ano_nascimento):  # método de classe, não de instância.
        # 'cls' é usado por convenção.
        idade = cls.ano_atual - ano_nascimento
        # ↑ variável interna ao método de classe
        return Pessoa(nome, idade)
    # como esse método é um construtor da classe, pode-se chamar de "factory method"

    @staticmethod  # ← indicado de método estático
    def gera_codigo():
        from random import randint
        codigo = randint(1, 1000)
        return codigo
    # o método estático nada mais é do que uma função normal que,
    # por organização, fica dentro da classe, mas que não importa
    # nada da função e nem da instância.

if __name__ == '__main__':
    pessoa_1 = Pessoa.por_ano_nascimento('João', 1988)
    # ↑ invocando o método para a criação de uma intância
    pessoa_2 = Pessoa.por_ano_nascimento('Zeca', 1975)
    print(pessoa_2.gera_codigo())

