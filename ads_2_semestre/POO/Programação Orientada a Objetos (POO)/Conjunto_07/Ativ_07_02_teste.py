from Ativ_07_02_classe import Ponto
import random

alfabeto = ["A","B","C","D","E","F","G","H","I","J"]
pontos = []
for i in alfabeto:
    i = Ponto.criar(f"Ponto {i},{random.randint(-100, 100)},{random.randint(-100, 100)}")
    pontos.append(i)
for i in pontos:
    print(i)
    