quantidade = 0
soma = 0

for i in range(6):
    n = float(input())
    if n > 0:
        quantidade += 1
        soma += n

print(f"{quantidade} valores positivos")
print(f"{soma / quantidade:.1f}")