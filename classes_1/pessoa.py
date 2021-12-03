from datetime import datetime


class Pessoa:  # Usar PascalCase por convenção (diferente de 'c'amel'C'ase).
    ano_atual = datetime.today().year
    # essa é uma variável cujo dado é constante para todas as instâncias
    # dessa classe que forem criadas.
    # chamada de "variável da classe" ou "variável estática".
    # o ano atual é o mesmo, independentemente da pessoa.
    # para usar essa variável, chame por self.ano_atual.

    def __init__(self, nome, idade, comendo=False, falando=False):
        # ↑ método 'construtor' da classe. Toda vez que instanciamos
        # uma classe (criamos um objeto daquela classe), esse método
        # é executado e seus parâmetros, se existirem, exigem os argumentos,
        # se estes não tiverem valores padrão.
        # desconsiderar o parâmetro 'self' ao lançar os argumentos.

        self.nome = nome
        self.idade= idade
        self.comendo = comendo
        self.falando = falando
        # ↑ definição das variáveis 'dinâmicas' da classe
        # essas variáveis representam os atributos passados
        # no método construtor.

    def falar(self, assunto):
        if self.falando:
            print(f'{self.nome} já está falando.')
            return
        if self.comendo:
            print(f'{self.nome} não pode falar enquanto come.')
            return
            # ↑ nesse caso, estou colocando o 'return' vazio
            # porque nada mais do método será executado se
            # a condição for atendida.

        self.falando = True
        print(f'{self.nome} agora está falando sobre {assunto}.')
        # ↑ essa parte é executada se a condição anterior não for atendida.

    def parar_de_falar(self):
        if not self.falando:
            print(f'{self.nome} já está calado.')
            return
        print(f'{self.nome} agora parou de falar.')
        self.falando = False

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return f'{self.nome} está comendo {alimento}.'
        if self.falando:
            print(f'{self.nome} não pode comer enquanto está falando.')
            return
        self.comendo = True
        print(f'{self.nome} agora está comendo {alimento}.')

    def parar_comer(self):
        self.comendo = False
        print(f'{self.nome} parou de comer.')

    def get_ano_nasc(self):
        ano_nasc = self.ano_atual - self.idade
        # ↑ usando a variável
        return ano_nasc

