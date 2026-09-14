def soma_dos_elementos(list):
    soma = 0
    for linha in list:
        for num in linha:
            soma += num
    print(soma)

def maior_elemento (list):
    bigger = None
    for linha in list:
        for num in linha:
            if (bigger == None or bigger < num):
                bigger = num
    print(bigger)
lista = []
matriz = [
    [],
    [],
    []
]

with open("Ativ_01_02.csv") as arq:
    for linha in arq:
        num_str = linha.strip().split(",")
        for num in num_str:
            lista.append(int(num))

cont = 0

while True:
    if(len(matriz[0]) !=3):
        matriz[0].append(lista[cont])
        cont +=1
    elif(len(matriz[1]) !=3):
        matriz[1].append(lista[cont])
        cont +=1
    elif(len(matriz[2]) !=3):
        matriz[2].append(lista[cont])
        cont +=1
    else:
        break;
soma_dos_elementos(matriz)
maior_elemento(matriz)