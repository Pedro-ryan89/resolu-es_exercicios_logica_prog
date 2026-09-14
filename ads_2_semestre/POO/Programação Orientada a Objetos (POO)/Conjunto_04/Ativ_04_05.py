# #5º QUESTÃO: Classe Carro: Crie uma classe que modele um carro:

# import random
# class Carro:
#     def __init__(self, marca, modelo, ano, cor, velocidade_atual):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano
#         self.cor = cor
#         self.velocidade_atual = velocidade_atual
#     def acelerar(self):
#         self.velocidade_atual += 10
#     def frear (self):
#         if(self.velocidade_atual <= 10):
#             self.velocidade_atual = 0
#         else:
#             self.velocidade_atual -= 10
#     def pintar(self):
#         cores = ["Preto", "Branco", "Prata", "Cinza", "Vermelho", "Azul", "Marrom", "Verde", "Amarelo", "Laranja"]
#         nova_cor = cores[random.randint(0, 9)]
#         while(nova_cor == self.cor):
#             nova_cor = cores[random.randint(0, 9)]
#         self.cor = nova_cor
#         print(f"A nova cor do seu carro é: {nova_cor}")
#     def mostrar_informacoes (self):
#         print(f"A marca é {self.marca}, modelo {self.modelo}, ano {self.ano}, da cor {self.cor}, com velocidade atual de {self.velocidade_atual}km/h")
#     def __str__(self):
#         return f"A marca é {self.marca}, modelo {self.modelo}, ano {self.ano}, da cor {self.cor}, com velocidade atual de {self.velocidade_atual}km/h"
# if (__name__ == "__main__"):

#     marca = input("Qual a marca do seu carro? \n")
#     modelo = input("Qual o modelo do seu carro? \n")
#     ano = input("Qual o ano do seu carro? \n")
#     cor = input("Qual a cor do seu carro? \n")
#     try:
#         velocidade_atual = float(input("Qual a velocidade atual do seu carro? \n"))
#     except:
#         print("Dê uma resposta váida.")

#     carro_motorista = Carro(marca, modelo, ano, cor, velocidade_atual)

#     while True:
#         while True:
#             try:
#                 print("1 - ACELERAR      2 - FREAR")
#                 print("3 - PINTAR        4 - MOSTRAR INFORMAÇÕES")
#                 print("       5 - SAIR DO CARRO       ")
#                 print(" ")
#                 escolha = int(input("O que você gostaria de fazer? \n"))
#                 if (1<=escolha<=5):
#                     break;
#                 else:
#                     print("Escolha uma opção válida.")
#                     print(" ")
#             except ValueError:
#                 print("Forma de resposta inválida.")
#                 print(" ")
#         if(escolha == 1):
#             carro_motorista.acelerar()
#             print(" ")
#         elif(escolha == 2):
#             if(carro_motorista.velocidade_atual == 0):
#                 print("Seu carro já está parado. \n")
#             else:
#                 carro_motorista.frear()
#             print(" ")
#         elif(escolha == 3):
#             carro_motorista.pintar()
#             print(" ")
#         elif(escolha == 4):
#             carro_motorista.mostrar_informacoes()
#             print(carro_motorista)
#             print(" ")
#         elif(escolha == 5):
#             if(carro_motorista.velocidade_atual > 0):
#                 print("Está tentando se matar? O carro ainda está em movimento!")
#                 print(" ")
#             else:
#                 print("Você saiu com sucesso e em segurança de seu carro.")
#                 break;
A = "Oi"
B = A
B = "Ava"
print(A)
