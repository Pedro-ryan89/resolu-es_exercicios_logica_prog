class ContaBancaria:
    def __init__(self, saldo, titular,cpf):
        self.saldo=saldo
        self.titular=titular
        self.cpf=cpf

Conta1 = ContaBancaria(1000, "Daniel","000.000.000-01")
print(Conta1.saldo)
print(Conta1.titular)
print(Conta1.cpf)


