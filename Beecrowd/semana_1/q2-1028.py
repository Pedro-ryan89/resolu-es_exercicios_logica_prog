# numero_de_trocas = int(input())

# contador = 0
# while contador < numero_de_trocas:
#     f1, f2 = map(int, input().split())

#     a = min(f1, f2)
#     for atual in range(a, 0, -1):
#         if f1 % atual == 0 and f2 % atual == 0:
#             print(atual)
#             break
#     contador += 1


# USAR ALGORITMO DE EUCLIDES

numero_de_trocas = int(input())

contador = 0
while contador < numero_de_trocas:
    f1, f2 = map(int, input().split())
    while f2 != 0:
        a = f1 % f2
        f1 = f2
        f2 = a
    print(f1)
    contador += 1
