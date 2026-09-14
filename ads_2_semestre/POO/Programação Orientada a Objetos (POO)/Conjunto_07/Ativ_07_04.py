#4º QUESTÃO: Crie uma classe Funcionário para armazenar as informações de um Funcionário. A classe
#deve armazenar o nome, o cargo o valor da hora trabalhada, a quantidade de horas
#trabalhadas e o salário. Esses dois últimos parâmetros não devem ser públicos.

class Funcionario:
    def __init__(self, nome, cargo, valor_hora=100):
        self.nome = nome
        self.cargo = cargo
        self.valor_hora = valor_hora
        self.__salario = 0
        self.__quantidade_horas = 0

    def registrar_hora(self):
        self.__quantidade_horas +=1
        self.calcular_salario()

    def calcular_salario (self):
        self.__salario = self.__quantidade_horas * self.valor_hora

    @property
    def salario(self):
        return f"R${self.__salario:.2f}"

    @salario.setter
    def salario(self, valor):
        raise Exception ("Não é permitido alterar o valor do salário manualmente")

if (__name__ == "__main__"):
    daniel = Funcionario("Daniel", "Programador")
    daniel.calcular_salario()
    print(daniel.salario)
    daniel.registrar_hora()
    daniel.calcular_salario()
    print(daniel.salario)