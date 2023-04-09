# Ex 003

class contaBancaria:
    def __init__(self, saldo, conta , titular):
        self.saldo = saldo
        self.conta = conta
        self.titular = titular
        self.sexo = "Masculino"

    def depositar(self,valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

contadojeff = contaBancaria(3.50,1234,"Jefferson")
print(contadojeff.saldo)
contadojeff.depositar(2000)
contadojeff.sacar(500)
print(contadojeff.saldo)
print(contadojeff.titular)
print(contadojeff.sexo)
