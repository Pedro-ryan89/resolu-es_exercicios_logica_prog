# ============================================================
# Lista de Exercícios 05 –  Listas e Dicionários
# IFCE – Tecnologia em Análise e Desenvolvimento de Sistemas
# ============================================================

#==============================================================
                    # Basicas
#=============================================================

# ======================== Questão 1 ========================
"""

nomes = ["Ana", "Bruno", "Carla", "Diego", "Eva"]
print(nomes[0],nomes[2],nomes[4])

"""
# ======================== Questão 2 ========================

"""
numeros = [int(input("adicione os valores: ")) for _ in range(3)]

print(numeros)
"""

# ======================== Questão 3 ========================

""""
cores = ["azul", "vermelho", "verde", "azul", "amarelo", "azul"]

print("=====================================")
cont_azul = 0
print(cores)
for i in cores:
    if i == "azul":
        cont_azul += 1       
print("=====================================")
    
print(f"vezes em que azul aparece: {cont_azul} ")
print(f"posição cor verde: {cores.index('verde')}")    
cores[1], cores[4] = cores[4],cores[1]
print(cores)

"""

# ======================== Questão 4 ========================

"""
frutas = ["maçã", "banana", "uva","banana", "pitomba", "cajá"]
frutas.insert(1,"laranja")
frutas.remove("banana")
print(frutas)
"""

# ======================== Questão 5 ========================

"""
valores = [10, 20, 30, 40, 50]

valores.pop(4)
valores.reverse()
print(valores)
"""

# ======================== Questão 6 ========================

"""
frutas = ["caju","banana","uva","abacaxi"]

frutas.append("morango")
frutas.insert(0,"goiaba")
frutas.pop(2)
print(frutas[2])
print(frutas)
print(len(frutas))

"""

# ======================== Questão 7 ========================

"""
n = [int(input("adicione os valores: ")) for _ in range(20)]

for i in range(0, 20 , 2):
    n[i], n[i + 1] = n [i + 1] , n[i]
print(n)
  
"""        
# ======================== Questão 8 ========================

"""
n = [1,2,3,4,5,6,7,8,9,10]
k = [10,20,30,40,50,60,70,80,90,100]

lista_m = []
for i in range(10):
    lista_m.append(n[i] - k[i])
print(lista_m)

"""

#======================================================
                 # Problemas
#======================================================

# ======================== Questão 1 ========================

"""
idades = []
alturas = []


for i in range(30):
    idade = int(input("insira idade: "))
    altura = float(input("insira altura: "))
    
    idade.append(idade)
    alturas.append(altura)


soma_altura = 0
for altura in alturas:
    soma_altura += altura

media =soma_altura / 30


contador = 0

for i in range(30):
    if idade[i] > 13 and altura[i] < media:
        contador += 1;
print("media alturas: ", media)
print("quantidade de alunos: ", contador)

"""

# ======================== Questão 2 ========================

'''
import random

contador = 0
lista = []


while contador < 1000:
    contador += 1
    a = random.randint(1,6)
    lista.append(a)

for _ in range(1,7):  
    print(f"O número {_} apareceu {lista.count(_)} vezes")

'''

# ======================== Questão 3 ========================

""""
playlist = ["rock", "pop", "rock", "jazz","pagode","bahiao","rock indie","samba","samba","alt","rock","pop","jazz"]
lista_sem_duplicadas = list(set(playlist))
print(lista_sem_duplicadas)
"""

# ======================== Questão 4 ========================

"""
A = [1,2,3,4,5]
B = [6,2,5,3,1]
C = []
D = list(set(A + B))

for i in A:
    if i in B: 
        C.append(i)

print(f"A: {A}")
print(f"B: {B}")
print(f"Interseção C: {C}")
print(f"União D: {D}")

"""

# ======================== Questão 5 ========================

"""
quantidade = [3,4,5]
preco = [12,12,12]
faturamento_total = 0
for i in range(len(quantidade)):
    faturamento = quantidade[i] * preco[i]
    faturamento_total += faturamento
print(faturamento_total)
"""
# ======================== Questão 6 ========================

"""
A = [2,4,5]
S = 0
contador = 0
for i in range(1,len(A) + 1):
    n = i / A[i - 1]
    S += n
    if i < A[i - 1]:
        contador += 1
        
print(S)
print(f"contador: {contador} ")

"""
# ======================== Questão 7 ========================

"""
A = [8,2,4,3,4,2,5,1]
B = [3,3,7,5,2,3,3,7]
resultado = []
vai_um = 0
soma = 0
for a,b in zip(A[::-1], B[::-1]):
    soma = a + b + vai_um
    vai_um = soma // 10
    resultado.append(soma % 10)
    
if vai_um > 0:
        resultado.append(vai_um)

print(A)
print(B) 
print("___________________________________")
print(resultado[::-1])

"""
 
# ======================== Questão 8 ========================

"""
# V = [-3,-1,10,12]
V = [-1,0,1,4,9]

if len(V) % 2 == 0:
    print((V[len(V) // 2 - 1] + V[len(V) // 2]) / 2)
else:
    print(V[len(V) // 2])
"""

# ======================== Questão 9 ========================

"""
Sequencia = [5, 2, -2, -7, 3, 14, 10, -3, 9, -6, 4, 1]
soma = 0
maior_soma = 0

for i in Sequencia:
    soma += i
    if soma > maior_soma and soma > 0:
        maior_soma = soma
    elif soma < 0:
        soma = 0
        
print(maior_soma)
"""

# ======================== Questão 10 ========================

#Bubble sort
"""
lista_sem_ordem = [5,3,2,4,1]

for i in range(len(lista_sem_ordem ) - 1  ):
    for j in range(len(lista_sem_ordem) - 1):
        if lista_sem_ordem[j] > lista_sem_ordem[j + 1]:
            lista_sem_ordem[j],lista_sem_ordem[j+ 1]  = lista_sem_ordem[j+ 1] ,lista_sem_ordem[j]
            
print(f"lista ordenada: {lista_sem_ordem}")
    
"""

#Selection Sort

""""
lista = [5,3,2,4,1]

lista_ordenada = []

while len(lista) > 0:

    menor = lista[0]
    for numero in lista:
        if numero < menor:
            menor = numero

    lista_ordenada.append(menor)

    lista.remove(menor)

print(lista_ordenada)

"""
# ======================== Questão 11 ========================

#busca binaria

"""
lista = [1, 3, 5, 7, 9, 11, 13,61,89,34,12,90,43,76,112]

lista.sort()

alvo = 61

inicio = 0
fim = len(lista) - 1

while inicio <= fim:

    meio = (inicio + fim) // 2

    if lista[meio] == alvo:
        print(f"Elemento encontrado na posição {meio}")
        break
    elif alvo < lista[meio]:
        fim = meio - 1
    else:
        inicio = meio + 1
    
"""

#======================================================
                 # Listas Bidimensionais:
#======================================================

# ======================== Questão 1 ========================

"""
matriz = [[],[],[],[]]
 
for linha in range(4):
    for coluna in range(4):
        matriz[linha].append(int(input()))

print(matriz)
"""
# ======================== Questão 2 ========================

"""

matriz = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,16]]

maior_valor = 0

for linha in matriz:
    for coluna in linha:
        if coluna > 10:
            maior_valor += 1
print(maior_valor)


"""

# ======================== Questão 3 ========================

"""
matriz = [[1,2],
          [3,4]]

for linha in matriz:
    for conluna in linha:
        calculo = matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]

print(calculo)    
"""

# ======================== Questão 4 ========================

"""
matriz = []

for linha in range(5):
    linha_atual = []
    for coluna in range(5):
        calculo = linha * coluna
        linha_atual.append(calculo)
    
    matriz.append(linha_atual)
        
print(f"{matriz}")

"""
# ======================== Questão 5 ========================

"""
matriz = [
        [1, 85, 67, 98],
        [5, 19, 70, 223],
        [9, 11, 456, 12],
        [13, 14, 15, 16]
    ]

maior_valor = matriz[0][0]

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        if matriz[linha][coluna] > maior_valor :
            maior_valor = matriz[linha][coluna]
            linha_maior = linha
            coluna_maior = coluna
print(f"coluna:{coluna_maior} linha:{linha_maior}, maior valor: {maior_valor}")

"""

# ======================== Questão 6 ========================

"""
matriz = [
        [1, 85, 67, 98,90],
        [5, 19, 70, 223,87],
        [9, 11, 456, 12,66],
        [13, 14, 15, 16,55],
        [45, 12,  34,56,24]
    ]

x = int(input("escolha valor na matriz: "))
valor_atual = matriz[0][0]
encontrado = False
for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        if matriz[linha][coluna] == x :
            encontrado = True
            valor_atual = x
            linha_encontrada = linha
            coluna_encontrada = coluna

if encontrado:
    print(f"encontrado: linha[{linha_encontrada}],coluna[{coluna_encontrada}]")
else:
    print("nao encontrado")
    
"""
#======================================================
                 # Dicionarios
#======================================================

# ======================== Questão 1 ========================

"""
dicionario = {
         "nome": "chico dede",
         "idade": "((9! / 8!)² − √36 × ln(e⁶))",
         "profissao": "programa em binario",
         "ablublebluble": "abuqibsdiban",
}

dicionario["nome"] = "sapao"
dicionario["idade"] = "78"
dicionario["profissao"] = "programa em assembly"
del dicionario['ablublebluble']
print(dicionario)

"""

# ======================== Questão 2 ========================

"""

chaves = ["nome","idade","cidade"]
valores = ["Pedro", 20,"itapipoca"]
dicionario = {}
for i in range(len(chaves)):
        dicionario[chaves[i]] = valores[i] 
print(dicionario)

"""

# ======================== Questão 3 ========================

dicionario = {}

for numero in range(1, 6):
    dicionario[numero] = numero ** 2

print(dicionario)