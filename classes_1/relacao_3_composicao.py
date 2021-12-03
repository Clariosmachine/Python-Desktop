"""
Na relação de composição um objeto 'instacia' o outro dentro dele,
assim, quando o objeto principal é apagado, os objetos instanciados
por ele são apgados também.
"""


class Computador():
    def __init__(self, processador, cap_memoria):
        self.processador = processador
        self.cap_memoria= cap_memoria
        self.hds = {}
        self.codigo = (x for x in range(10))

    def insere_hd(self, marca, capacidade):
        disco = Hd(marca, capacidade)
        self.hds[next(self.codigo)] = [disco.marca, disco.capacidade]

    def __del__(self):  # método para ver quando o objeto é apagado
        print('Objeto Computador foi apagado')
    

class Hd():
    def __init__(self, marca, capacidade):
        self.marca = marca
        self.capacidade = capacidade

    def __del__(self):
        print('Objeto Hd foi apagado')


computador_teste = Computador('Ryzen 3600', '4 GB')
computador_teste.insere_hd('Seagate', '500GB')
computador_teste.insere_hd('Barracuda', '1TB')
print(computador_teste.hds)
print('#'*30)
# ↑ identificando o fim do código
