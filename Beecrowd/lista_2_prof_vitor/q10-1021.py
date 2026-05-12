n = float(input())

conv = int(round(n * 100))

cedulas = [10000,5000,2000,1000,500,200]
centavos = [100,50,25,10,5,1]

print("NOTAS:")
for i in cedulas:
    qtd_cedulas = conv // i
    nv_cedulas = conv % i
    print(f"{qtd_cedulas} notas(s) de R${i/100:.2f}")
        
print("MOEDAS:")
for j in centavos:
    qtd_centavos = conv // j
    nov_centavos = conv % j
    print(f"{qtd_centavos} moedas(s) de R${j/100:.2f}")
    