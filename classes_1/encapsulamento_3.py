"""
[Public, protected, private]
O Python trata, no geral, tudo como público, mas há convenções
que ajudam a proteger o código ao compartilhar ou trabalhar em grupo.
Use-se o Underline (_) para tratar um método ou atributo como 'protected';
Usa-se dois underlines (__) para que o Python trate o atributo ou
método como privado.
"""


class BancoDeDados:
    def __init__(self):
        self.__clientes = {}

    def add_clientes(self, codigo, nome):
        self.__clientes[codigo] = nome

    def mostra_clientes(self):
        for x, y in self.__clientes.items():
            print(x, ':', y)


cadastros = BancoDeDados()
cadastros.add_clientes(1, 'João')
cadastros.add_clientes(2, 'Maria')
# print(cadastros.__clientes)
# ↑ é impossível esse comando dar certo aqui, porque o atributo é privado,
# e ele só pode ser acessado de dentro da classe.
cadastros.mostra_clientes()
# Esse método mostra o que quero porque ele pegou os valores enquanto estava dentro da classe.

"""
Nesse caso, eu deixe o atributo clientes privado. Assim, ao tentar acessar
ele, a linguagem não me permitiu, informou que ele não existe.
Dessa forma o programador não consegue alterar esse atributo de fora.
"""