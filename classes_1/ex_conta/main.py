from classes_1.ex_conta.conta import Conta

conta = Conta('João', 123456, 0, 1000)
conta.deposita(999)
conta.saca(99)
conta.extrato()
print()
conta2 = Conta('Silvio', 1234, 0, 1000)
conta2.deposita(100)
print()
conta2.transfere_para(conta2, 100)
print()
conta.extrato()
conta2.extrato()