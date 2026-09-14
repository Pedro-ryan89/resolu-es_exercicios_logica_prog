# ============================================================
# Lista de Exercícios 02 - CLASSES E OBJETOS
# IFCE - Tecnologia em Analise e Desenvolvimento de Sistemas
# ============================================================


# ======================== Questão 1 ========================

# class Livro:
#     def __init__(self,titulo: str,autor: str,total_paginas:int,pagina_atual:int):
#         self.titulo = titulo
#         self.autor = autor
#         self.total_paginas = total_paginas
#         self.pagina_atual = pagina_atual
        
#     def avancar_pagina(self):
#         self.pagina_atual += 1
    
#     def voltar_pagina(self):
#         if self.pagina_atual > 0:
#             self.pagina_atual -= 1
        
        
#     def ir_para_pagina(self,pag):
#         if pag > 0  and pag <= self.total_paginas:
#             self.pagina_atual = pag
#         else:
#             print("numero da pagina e maior que o limite de paginas do livro")
    
#     def __str__(self):
#         return f"livro: {self.titulo},autor: {self.autor},total de paginas: {self.total_paginas}, pagina_atual: {self.pagina_atual}"

# livro = Livro("teste","teste da silva",100,10)
# livro.avancar_pagina()
# print(livro)
# livro.ir_para_pagina(80)
# print(livro)

# ======================== Questão 2 ========================

# class Stopwatch:
#     def __init__(self):
#         self.seconds = 0
#         self.minutes = 0
        
#     def tick(self):
#         self.seconds += 1
#         if self.seconds > 59:
#             self.seconds = 0
#             self.minutes += 1
#         if self.minutes > 59:
#             self.seconds = 0
#             self.minutes = 0

#     def __str__(self):
#         return f"{self.minutes:02d}:{self.seconds:02d}"
    
# watch = Stopwatch()
# for i in range(3600):
#     print(watch)
#     watch.tick()


# ======================== Questão 3 ========================

# import time
# class Clock:
#     def __init__(self,horas:int = 0,minutos:int = 0,segundos: int = 0):
#         self.horas = horas
#         self.minutos = minutos
#         self.segundos = segundos
        

#     # adicionar 1 segundo ao relogio
#     def tick(self):
#         self.segundos += 1
#         if self.segundos > 59:
#             self.segundos = 0
#             self.minutos += 1
#         if self.minutos > 59:
#             self.minutos = 0
#             self.horas += 1
#         if self.horas > 23:
#             self.segundos = 0
#             self.minutos = 0
#             self.horas = 0

#     #definir novos valores e zerar os segundos
    
#     def set(self,nova_hora,nova_minutos):
#         self.horas = nova_hora
#         self.minutos = nova_minutos
#         self.segundos = 0


#     def __str__(self):
#         return f"{self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}"


# clock = Clock(0, 0, 0)


# for i in range(86406):
#     print(clock) 
#     clock.tick()
#     time.sleep(1)

# ======================== Questão 4 ========================


# class LunchCard:
#     def __init__(self,saldo:int = 0):
#         self.saldo = saldo
    
#     def eat_lunch(self):
#         if self.saldo < 2.60:
#             print("saldo insuficiente")
#         else:
#             self.saldo -= 2.60
            
#     def eat_special(self):
#         if self.saldo < 4.60:
#             print("saldo insuficiente")
#         else:
#             self.saldo -= 4.60
            
#     def deposit_money(self,amount):
#         if amount < 0:
#             raise ValueError("valor e menor que zero") 
#         else:
#             self.saldo += amount
                       
#     def __str__(self):
#         return f"The Balance is {self.saldo:.1f}"
    
# card_peter = LunchCard(0)
# card_grace = LunchCard(30)
# print("==========PETER=============")
# card_peter.eat_special() # 15.4
# print(card_peter)
# card_peter.deposit_money(20)  #15.4 + 20
# print(card_peter)
# card_peter.eat_lunch()
# card_peter.eat_lunch()
# print(card_peter)

# print("==========GRACE==============")
# card_grace.eat_lunch() #27.4
# print(card_grace)
# card_grace.eat_special()
# print(card_grace)
# card_grace.deposit_money(50) # 27.4 + 50
# print(card_grace)

# ======================== Questão 5 ========================

# class LunchCard:
#     def __init__(self,balance: float):
#         self.balance = balance
    
#     def deposit_money(self,amount: float):
#         self.balance += amount
    
#     def substract_from_Balance(self,amount: float) -> bool:
#         if self.balance >= amount:
#             self.balance -= amount
#             return True
#         else:
#             return False
        
        
# class PaymentTerminal:
#     def __init__(self):
#         self.funds = 1000
#         self.lunches = 0
#         self.specials = 0
    
#     def eat_lunch(self,payment: float) -> float:
#         if payment >= 2.50:
#             self.lunches += 1
#             self.funds += 2.50
#             return payment - 2.50
#         else:
#             return payment
    
#     def eat_special(self,payment: float) -> float:
#         if payment >= 4.30:
#             self.specials += 1
#             self.funds += 4.30
#             return payment - 4.30
#         else:
#              return payment
    
#     def eat_lunch_lunchcard(self,card: LunchCard) -> bool:
#         if card.balance >= 2.50:
#             self.lunches += 1
#             card.balance -= 2.50
#             return True
#         else:
#             return False
    

#     def eat_special_lunchcard(self,card: LunchCard) ->  bool:
#         if card.balance >= 4.30:
#             self.specials += 1
#             card.balance -= 4.30
#             return True
#         else:
#             return False
    
#     def deposit_money_on_card(self, card: LunchCard,sum: float):
#         if sum <= 0:
#             raise ValueError("deposite valores acima de 0")
#         else:
#             card.balance += sum
#             self.funds += sum
        

# exactum = PaymentTerminal()

# card = LunchCard(2)
# print(f"Card balance is {card.balance} euros")

# result = exactum.eat_special_lunchcard(card)
# print("Payment successful:", result)

# exactum.deposit_money_on_card(card, 100)
# print(f"Card balance is {card.balance} euros")

# result = exactum.eat_special_lunchcard(card)
# print("Payment successful:", result)
# print(f"Card balance is {card.balance} euros")

# print("Funds available at the terminal:", exactum.funds)
# print("Regular lunches sold:", exactum.lunches)
# print("Special lunches sold:", exactum.specials)

# ======================== Questão 6 ========================

class Personagem:
    def __init__(self,nome: str,vida:int = 100,ataque:int = 10,nivel:int = 1):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.nivel = nivel
        
    
    def atacar(self,inimigo: "Personagem"):
        inimigo.receber_dano(self.ataque)
    
    def receber_dano(self,dano: int):
        self.vida -= dano
    
    def subir_nivel(self):
        self.nivel += 1
        self.ataque += 5
        self.vida += 20

    def __str__(self):
        return f"Nome {self.nome} | Nivel: {self.nivel} | Vida: {self.vida} | Ataque: {self.ataque}"


rockeiro = Personagem("Rockeiro", 120,12,1)
pirangueiro = Personagem("Pirangueiro", 150, 15,1)
 
rockeiro.atacar(pirangueiro)
print(f"{rockeiro.nome} atacou {pirangueiro.nome} causando {rockeiro.ataque} de dano!")
print(f"{pirangueiro.nome} agora tem {pirangueiro.vida} de vida")

pirangueiro.atacar(rockeiro)
print(f"{pirangueiro.nome} atacou {rockeiro.nome} causando {pirangueiro.ataque} de dano")
print(f"{rockeiro.nome} agora tem {rockeiro.vida} de vida")

rockeiro.subir_nivel()
print(f"{rockeiro.nome} subiu para o nivel {rockeiro.nivel} Ataque aumentado para {rockeiro.ataque}, Vida agora e {rockeiro.vida}")
print(rockeiro)

