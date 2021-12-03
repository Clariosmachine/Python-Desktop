"""
[Public, protected, private]
↑ Estes são os três estados em que podem ser encontrados os atributos
ou os métodos das classes nas linguagens de programação comuns.
Esses status vão de encontro à filisofia do Python, que trata todos os
programadores como adultos que sabem o que estão fazendo.
"""


class BancoDeDados:
    def __init__(self):
        self.clientes = {}

    def add_clientes(self, codigo, nome):
        self.clientes[codigo] = nome

    def mostra_clientes(self):
        for x, y in self.clientes.items():
            print(x, ':', y)


cadastros = BancoDeDados()
cadastros.add_clientes(1, 'João')
cadastros.add_clientes(2, 'Maria')
cadastros.mostra_clientes()


"""
Public → atributo ou método que pode ser acessado e alterado de fora da classe;
Protected → atributo ou método que pode ser acessado e alterado pela classe ou suas filhas;
Private → atributo ou método que pode ser acessado e alterado apenas de dentro da classe 
"""