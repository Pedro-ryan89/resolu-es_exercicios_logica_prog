#1° QUESTÃO: Classe Livro: Crie e teste uma classe que modele um livro:
class Livro:
    def __init__(self, titulo: str, autor: str, total_paginas: int, pagina_atual: int):
        self.titulo = titulo
        self.autor = autor
        self.total_paginas = total_paginas
        self.pagina_atual = pagina_atual
    def __str__(self):
        return f"O livro {self.titulo}, do(a) escritor(a) {self.autor} tem {self.total_paginas} páginas , atualmente está na página {self.pagina_atual} \n"
    def avancar_pagina (self):
        if(self.pagina_atual == self.total_paginas):
            print("Você já está na última página. \n")
        else:
            self.pagina_atual +=1
    def voltar_pagina (self):
        if(self.pagina_atual == 1):
            print("Você está na primeira página, não tem como voltar páginas. \n")
        else:
            self.pagina_atual -=1
    def ir_para_pagina(self, escolha):
        if(1<=escolha<=self.total_paginas):
            self.pagina_atual = escolha
        else:
            print("Número da página inválida.")

if (__name__ == "__main__"):
    dracula = Livro("Drácula","Bram Stoker", 650, 1)
    print(dracula)
    dracula.avancar_pagina()
    print(dracula)
    dracula.voltar_pagina()
    print(dracula)
    dracula.ir_para_pagina(-1)
    dracula.ir_para_pagina(50)
    print(dracula)
print(" ")

#2° QUESTÃO: Classe Cronômetro (Stopwatch): Considere a seguinte estrutura para a classe Stopwatch:
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
    def tick(self):
        if(self.seconds == 59):
            self.minutes +=1
            self.seconds = 0
        else:
            self.seconds +=1
        if(self.minutes > 59):
            self.minutes = 0
            self.hours +=1
if(__name__ == "__main__"):
    watch = Stopwatch()
    for i in range(3601):
        print(watch)
        watch.tick()
print(" ")

#3° QUESTÃO: Defina uma nova classe chamada Clock que expanda as capacidades da sua classe Stopwatch. 
# Ela deve funcionar da seguinte forma:


class Clock:
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours
    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
    def tick(self):
        if(self.seconds == 59):
            self.minutes +=1
            self.seconds = 0
        else:
            self.seconds +=1
        if(self.minutes > 59):
            self.minutes = 0
            self.hours +=1
        if(self.hours == 24):
            self.hours = 0
    def set(self, new_hour = 0, new_minute = 0, new_second = 0):
        self.hours = new_hour
        self.minutes = new_minute
        self.seconds = new_second


if (__name__ == "__main__"):
    clock = Clock(23, 59, 55)
    for i in range(6):
        print(clock)
        clock.tick()
    clock.set(12,5)
    print(clock)
print(" ")

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
print(" ")

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
print(" ")

#6º QUESTÃO:Classe Personagem: Criando um Sistema de Batalha

class Personagem:
    def __init__(self, nome: str, vida: int = 100, ataque: int = 10, nivel: int = 1):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.nivel = nivel
    def __str__(self):
        return f"Nome: {self.nome} | Nível: {self.nivel} | Vida: {self.vida} | Ataque: {self.ataque}"
    def receber_dano (self, vilão: "Personagem"):
        self.vida -= vilão.ataque
        if(self.vida > 0):
            print(f"{self.nome} agora tem {self.vida} de vida.")
        else:
            print(f"{self.nome} foi derrotado!")
    def atacar (self, inimigo: "Personagem"):
        print(f"{self.nome} atacou o {inimigo.nome} causando {self.ataque} de dano!")
        inimigo.receber_dano(self)
    def subir_nivel(self):
        self.nivel +=1
        self.ataque +=5
        self.vida +=20
        return f"{self.nome} evoluiu para o nível {self.nivel}!"

rockeiro = Personagem("Rockeiro", 120, 12)
pirangueiro = Personagem("Pirangueiro", 150, 15)
rockeiro.atacar(pirangueiro)
pirangueiro.atacar(rockeiro)
rockeiro.subir_nivel()
print(rockeiro)
