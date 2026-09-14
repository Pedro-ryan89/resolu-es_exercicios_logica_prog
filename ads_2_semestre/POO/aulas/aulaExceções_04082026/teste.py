# try:
#     idade = int(input("digite sua idade: "))
# except ValueError:
#     idade = -1

# if idade>=0 and idade<=150:
#     print("idade valida")
# else:
#     print("idade invalida")




# def calcular_fatorial(n: int) -> int:
#     if n < 0:
#         raise ValueError(f"Entrada invalida: {n}. Use n>=0")


#     resultado = 1
#     for i in range(2,n+1):
#         resultado *= i

#     return resultado


# print(calcular_fatorial(5))
# print(calcular_fatorial(-1))


#------------------------------------------------------------------

# def ler_entrada(msg: str, min: int, max: int) -> int:
#     while True:
#         try:
#             numero = int(input(f"{msg} {min} e {max}: "))

#             if min <= numero <= max:
#                 return numero

#             print("Número fora do intervalo.")

#         except ValueError:
#             # print("Digite um número válido.")
#             pass


# numero = ler_entrada("Digite um número entre", 5, 10)
# print("Você digitou:", numero)

#------------------------------------------------------------------

# import math

# def hipotenusa(cateto01: float,cateto02: float) -> float:
#     return math.sqrt(cateto01**2 + cateto02**2)

# print(hipotenusa(3,5))

# from random import randint

# print("Dado: ",randint(1,6))


# import random

# def numero_loteria (qtd,menor,maior):
#     # for i in range(qtd):
#     #     print(random.randint(menor,maior))
#     return random.sample(range(menor, maior + 1), qtd)

# print(numero_loteria(6,1,60))
# # (numero_loteria(6,1,60))


# from datetime import datetime

# agora = datetime.now()
# print(agora)

# natal = datetime(2026, 12,25)
# print(natal)
# print(natal.day,natal.month,natal.year)
# print(natal - agora)

# import csv

# with open("frutas.csv", encoding="utf-8") as arq:
#     for linha in csv.reader(arq, delimiter=";"):
#         print(linha)

# import json

# with open("/home/pedro-ryan89/Documents/ads_2_semestre/POO/aulaExceções_04082026/teste.json", encoding="utf-8") as arq:
#     dados = json.load(arq)

# for usuario in dados["usuarios"]:
#     print(usuario["nome"])

import urlib.request, json

with urlib.request.urlopen
