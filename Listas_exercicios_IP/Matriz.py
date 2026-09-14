"""

matriz = [[1,2,3],          
          [4,5,6],          
          [7,8,9]]          
          
for i in range(3):
    for j in range(3):
        print(matriz[i][j])

"""

"""
n = int(input())

matriz = []
for i in range(n):
    linha = []
    for j in range(n):
        linha.append(0)
    matriz.append(linha)

for linha in matriz:
    print(linha)
"""

mt = [[0 for _ in range(5)] for _ in range(5)]
for x in range(5):
    for y in range(5):
        if y==0 or x==y:
            mt[x][y]=1
        else:
            mt[x][y]=mt[x-1][y]+mt[x-1][y-1]


for _ in mt:
    print(_)
