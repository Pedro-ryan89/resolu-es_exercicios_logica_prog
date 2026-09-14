#ENCONTRAR O MAIOR NÚMERO EM UM ARQUIVO
def maior(list):
    bigger = None
    for num in list:
        if(bigger == None or bigger < num):
            bigger = num
    print(f"O maior número é: {bigger}")

matriz = []

with open("Ativ_01_01.csv") as arq:
    for linha in arq:
        num_str = linha.strip().split(",")
        for num in num_str:
            matriz.append(int(num))
maior(matriz)