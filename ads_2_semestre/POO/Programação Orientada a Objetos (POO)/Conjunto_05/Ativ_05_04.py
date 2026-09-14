#4° QUESTÃO: Crie uma nova classe chamada LunchCard

class LunchCard:
    def __init__(self, salario_inicial):
        self.salario_inicial = salario_inicial
    def __str__(self):
        return f"The balance is {self.salario_inicial:.1f} euros"
    def eat_lunch(self):
        if(self.salario_inicial >= 2.60):
            self.salario_inicial -= 2.60
        else:
            print("Dinheiro insuficiente.")
    def eat_special(self):
        if(self.salario_inicial >=4.60):
            self.salario_inicial -= 4.60
        else:
            print("Dinheiro insuficiente.")
    def deposit_money(self, amount):
        if(amount < 0):
            raise ValueError("Valor errado.")
        else:
            self.salario_inicial += amount
        

if (__name__ == "__main__"):
    peter = LunchCard(20)
    grace = LunchCard(30)
    peter.eat_special()
    grace.eat_lunch()
    print(f"Peter: {peter} \n")
    print(f"Grace: {grace} \n")
    peter.deposit_money(20)
    grace.eat_special()
    print(f"Peter: {peter} \n")
    print(f"Grace: {grace} \n")
    peter.eat_lunch()
    peter.eat_special()
    grace.deposit_money(50)
    print(f"Peter: {peter} \n")
    print(f"Grace: {grace} \n")