n = int(input())
respostas = []

for i in range(n):
    k = int(input())
    if k == 0:
        respostas.append("NULL")
    else:
        if k % 2 == 0:
            tipo = "EVEN"
        else:
            tipo = "ODD"

        if k > 0:
            sinal = "POSITIVE"
        else:
            sinal = "NEGATIVE"
        respostas.append(f"{tipo} {sinal}")

for resposta in respostas:
    print(resposta)
