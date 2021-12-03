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
        self._clientes = {}

    def add_clientes(self, codigo, nome):
        self._clientes[codigo] = nome

    def mostra_clientes(self):
        for x, y in self._clientes.items():
            print(x, ':', y)


cadastros = BancoDeDados()
cadastros.add_clientes(1, 'João')
cadastros.add_clientes(2, 'Maria')
print(cadastros._clientes)
cadastros._clientes = 'Outra coisa'
print(cadastros._clientes)  # Eu ainda posso alterar totalmente aquele atributo ou método.
# ↑ Essa alteração impossibilita a execução do método a baixo porque não existe mais o dicionário.
#cadastros.mostra_clientes()


"""
Nesse caso, eu deixe o atributo clientes protegido. Assim, ao tentar acessar
ele, a linguagem não me 'recomendou', não auto-completou ao fazer a digitação.
Dessa forma o programador já fica avisado sobre aquele método ou atributo.
"""