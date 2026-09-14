class Conta:
    def __init__(self, saldo):
        self.__saldo = saldo
    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor
        else:
            raise ValueError("Saldo não pode ser negativo")

conta1 = Conta(100)
conta2 = Conta(200)
conta1.saldo = -100
print(conta1.saldo)