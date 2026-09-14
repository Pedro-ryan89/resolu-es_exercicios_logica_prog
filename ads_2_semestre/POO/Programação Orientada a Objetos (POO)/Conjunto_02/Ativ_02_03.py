import random

def numeros_loteria (quantidade, menor, maior):
    return random.sample(range(menor, maior + 1), quantidade)
print(numeros_loteria(6, 1, 60))