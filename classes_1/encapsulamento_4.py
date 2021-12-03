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

    @property
    def val_clientes(self):
        """
        Criando uma espécie de 'alias' para acessar os valores
        do atributo privado de fora da classe por meio de um getter.
        Mesmo assim não é possível alterar esse atributo, apenas visualizar os valores.
        """
        return self.__clientes

    def add_clientes(self, codigo, nome):
        self.__clientes[codigo] = nome

    def mostra_clientes(self):
        for x, y in self.__clientes.items():
            print(x, ':', y)


cadastros = BancoDeDados()
cadastros.add_clientes(1, 'João')
cadastros.add_clientes(2, 'Maria')
cadastros.clientes = 'Outra coisa'  # ← Não altera o __clientes, cria um novo atributo
print(cadastros.clientes)
# ↑ Aqui eu estou mostrando esse atributo que acabou de ser criado, mas não alterei em nada o __clientes.
cadastros.mostra_clientes()
# Esse método mostra o que quero porque ele pegou os valores enquanto estava dentro da classe.

"""
Algo que pode ser feito para acessar os valores desse atributo privado, é a criação de um 'alias'
por meio do @property, criando um getter. Ex: ↓
"""

print(cadastros.val_clientes)

"""
Outra maneira de acessar esse atributo é através de seu 'nome original' que
a linguagem cria quando um atributo privado é criado (__NomeDoAtributo).
Esse nome é composto de um underline + o nome da classe + o nome do atributo ou método
com os dois underlines. Nesse caso é _BandoDeDados__clientes. Ex: ↓
"""

print(cadastros._BancoDeDados__clientes)

# cadastros.val_clientes = 'teste de alteração'
# ↑ AttributeError: can't set attribute
