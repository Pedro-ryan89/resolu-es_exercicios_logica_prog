#5º QUESTÃO: Um LunchCard mais simples

class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance
    def __str__(self):
        return f"The balance is {self.salario_inicial:.1f} euros"
    def deposit_money(self, amount: float):
        if(amount < 0):
            raise ValueError("Valor errado.")
        else:
            self.balance += amount
    def subtract_from_balance(self, amount: float) -> bool:
        if(amount > self.balance):
            return False
        else:
            self.balance -= amount
            return True

class PaymentTerminal:
    def __init__(self):
        self.fund = 1000
        self.lunch = 0
        self.special = 0
    def eat_lunch(self, payment: float) -> float:
        if(payment >= 2.5):
            self.lunch +=1
            self.fund += 2.5
            return payment - 2.50
        else:
            pass
    def eat_lunch_lunchcard(self, card: LunchCard) -> bool:
        if(card.balance >= 2.5):
            self.lunch +=1
            card.balance -= 2.5
            return True
        else:
            return False
    def eat_special_lunchcard(self, card: LunchCard) -> bool:
        if(card.balance >= 4.3):
            self.special +=1
            card.balance -=4.3
            return True
        else:
            return False
    def eat_special(self, payment: float) -> float:
        if(payment >= 4.3):
            self.special +=1
            self.fund += 4.3
            return payment - 4.3
        else:
            pass
    def deposit_money_on_card (self, card: LunchCard, sum: float):
        if (sum >= 0):
            card.balance += sum
            self.fund += sum
        else:
            pass
if __name__ == "__main__":
    card = LunchCard(10)
    print("Balance", card.balance)
    result = card.subtract_from_balance(8)
    print("Payment successful:", result)
    print("Balance", card.balance)
    result = card.subtract_from_balance(4)
    print("Payment successful:", result)
    print("Balance", card.balance)
    exactum = PaymentTerminal()
    change = exactum.eat_lunch(10)
    print("The change returned was", change)
    change = exactum.eat_lunch(5)
    print("The change returned was", change)
    change = exactum.eat_special(4.3)
    print("The change returned was", change)
    print("Funds available at the terminal:", exactum.fund)
    print("Regular lunches sold:", exactum.lunch)
    print("Special lunches sold:", exactum.special)
    exactum = PaymentTerminal()
    change = exactum.eat_lunch(10)
    print("The change returned was", change)
    card = LunchCard(7)
    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)
    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)
    result = exactum.eat_lunch_lunchcard(card)
    print("Payment successful:", result)
    print("Funds available at the terminal:", exactum.fund)
    print("Regular lunches sold:", exactum.lunch)
    print("Special lunches sold:", exactum.special)
    exactum = PaymentTerminal()
    card = LunchCard(2)
    print(f"Card balance is {card.balance} euros")
    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)
    exactum.deposit_money_on_card(card, 100)
    print(f"Card balance is {card.balance} euros")
    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)
    print(f"Card balance is {card.balance} euros")
    print("Funds available at the terminal:", exactum.fund)
    print("Regular lunches sold:", exactum.lunch)
    print("Special lunches sold:", exactum.special)