class Animal:
    def __init__(self, especie, nome, idade, teste=None):
        # ↓ estes são os atributos. Os argumentos acima são apenas argumentos.
        self.especie = especie
        self.nome = nome
        self.idade = idade

    def get_especie(self):
        print('usado o método get.especie')
        return self.especie

    # Getter
    @property
    def teste_especie(self):  # ← usar o mesmo nome do atributo (fiz diferente para testar e deu certo)
        return self._especie + '_getter'  # usar underline antes do nome do atributo (evita loop infinito)
    # com esse getter, eu estou pegando o valor do que é trabalhado no setter
    # e enviando ele para o atributo (self.especie)

    # Setter
    @teste_especie.setter  # ← mesmo nome do getter, acrescentando o '.setter'
    def especie(self, valor):  # definindo o valor para o atributo da classe
        # o nome desse método tem que ser exatamente igual ao nome do atributo, sem o 'self.'
        # Esse 'valor' é o que foi enviado originalmente como
        # argumento para o atributo no momento da instanciação.
        self._especie = valor + '_setter'

    # ↓ modo limpo de utilizar getter e setter
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, teste):
        self._nome = teste.upper()  # alterando apenas o formato da string

cachorro = Animal('cão', 'Rex', 3)
print(cachorro.get_especie())  # usando o método criado para trazer o atributo
print(cachorro.teste_especie)  # usando o getter
print(cachorro.especie)  # usando o atributo
print()
print(cachorro.nome)


# todos os prints trazem o mesmo resultado: cão_setter_getter


# em resumo: o getter precisa da definição do método setter, que é interno (slave) do getter.
# o setter pega o atributo (self.atributo) trabalha com ele e passa ele lapidado para o getter.
# o getter pode apenas retornar o valor que foi refinado pelo setter ou, se precisar,
# o getter também pode executar algum trabalho sobre o valor antes de retornar ele.

# o único ponto, exatamente, em que é definido o atributo o qual se está trabalhando
# é na definição do setter 'def atributo(self, variável)'
# essa 'variável', que pode ter qualquer nome, traz o valor atribuído ao atributo.
