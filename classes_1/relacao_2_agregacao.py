"""
A agregação é um tipo de associação em que há pelo menos um
objeto que, essencialmente, precisa de outro.
"""


class CarrinhoDeCompras():
    def __init__(self):
        self.__produtos = []

    def inserir_produto(self, produto):
        self.__produtos.append(produto)

    def soma_total(self):
        soma = 0
        for item in self.__produtos:
            soma += item.preco
        return soma

    def mostra_itens(self):
        for item in self.__produtos:
            print(item.descricao)

    def __del__(self):
        print('Objeto CarrinhoDeCompras foi apagado')

class Produto():
    def __init__(self, descricao, preco):
        self.__descricao = descricao
        self.__preco = preco

    @property
    def descricao(self):
        return self.__descricao.upper().strip()

    @property
    def preco(self):
        x = str(self.__preco)
        return float(x.replace(',', '.').strip())

    def __del__(self):
        print('Objeto produto foi apagado')
        # ↑ Método para ver quando o objeto deixa de ser usado
        # no caso da agregação, apagar o objeto que usa esse outro não apaga esse outro.


carrinho_1 = CarrinhoDeCompras()
p1 = Produto('moto de brinquedo', 10.35)
p2 = Produto('boneca', '15,50')
carrinho_1.inserir_produto(p2)
carrinho_1.inserir_produto(p1)
carrinho_1.inserir_produto(p2)
print(carrinho_1.soma_total())
carrinho_1.mostra_itens()
del carrinho_1
print(p1.descricao)  # O objeto p1 ainda existe, mesmo depois de o carrinho ter sido apagado.
print('#'*30)
"""
Nesse caso a classe CarrinhoDeCompras depende da Produto para qualquer atividade,
embora a classe Produto não precisa em nada da outra.
"""