class Conta():
    def __init__(self, titular, numero, saldo, limite):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
        self.limite = limite

    def deposita(self, valor):
        if self.saldo + valor > self.limite:
            print(f'O valor não pode ser depositado na conta de {self.titular} porque ultrapassaria o limite da conta.')
            return False
        else:
            self.saldo += valor
            print(f'Foram depositados R$ {valor:0.2f} na conta de {self.titular}.')
            return True

    def saca(self, valor):
        if self.saldo - valor < 0:
            print('Valor solicitado indisponível.')
            return False
        else:
            self.saldo -= valor
            print(f'Foram retirados R$ {valor:0.2f} da conta de {self.titular}.')
            return True

    def extrato(self):
        print(f'O saldo atual da conta de {self.titular} é de R$ {self.saldo:0.2f}.')

    def transfere_para(self, conta_destino, valor):
        retirada = deposito = False
        if self.saca(valor):
            retirada = True
            if conta_destino.deposita(valor):
                deposito = True
            else:
                print(f'Estorno de débito da conta de {self.titular}:')
                self.deposita(valor)
        else:
            return None
        if retirada and deposito:
            print('transação realizada')
