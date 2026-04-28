valor = int(input())

if valor % 2 == 0:
    valor += 1

for i in range(6):
    print(valor + i * 2)