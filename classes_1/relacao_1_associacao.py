"""
Na relação de associação um objeto pode existir sem o outro,
ma existe a possibilidade de um deles usar uma instância do outro.
"""


class Bombeiro():
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None

    @property
    def nome(self):
        return (self.__nome + '_getter').upper()

    @nome.setter
    def nome(self, valor):
        self.__nome = valor + '_setter'

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, _ferramenta):
        self.__ferramenta = _ferramenta


class Veiculo():
    combust = 'gasolina'
    def __init__(self, tipo, placa):
        self.__tipo = tipo
        self._placa = placa


    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, _tipo):
        self.__tipo = _tipo.upper()


bombeiro_1 = Bombeiro('Jackson')
print(bombeiro_1.nome)
bombeiro_1.nome = 'João'
print(bombeiro_1.nome)
bombeiro_1.ferramenta = Veiculo('camihão', 'orh6375')
# ↑ criando um objeto da classe veículo associado ao objeto bombeiro
print(bombeiro_1.ferramenta._placa)

bombeiro_1.ferramenta.combust = 'água'
print(bombeiro_1.ferramenta.combust)
print(bombeiro_1.ferramenta.tipo)
print(Veiculo.combust)
