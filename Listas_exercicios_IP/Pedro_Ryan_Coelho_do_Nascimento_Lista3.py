#Questão 1

"""
numero = int(input("insira numero: "))

impar_par = numero % 2

if impar_par == 0:
    print("numero e par")
else:
    print("numero e impar")

"""

#Questão 2

"""
p_numero = int(input("primeiro numero: "))
s_numero = int(input("segundo numero: "))

multiplo = p_numero % s_numero

if multiplo == 0:
    print(f"{p_numero} e multiplo de {s_numero}")
else:
    print(f"{p_numero} nao e multiplo de {s_numero}")
"""

# Questão 3

"""

numero = int(input("insira o numero: "))

if numero % 3 == 0 and numero % 5 == 0:
    print("FizzBuzz")
elif numero % 3 == 0:
    print("Fizz")
elif numero % 5 == 0:
    print("Buzz")
   
"""
    
#Questão 4

"""
n_candidatos = int(input("numero de candidatos: ")) 

lista_candidatos = []
for _ in range (n_candidatos):
    candidatos = input(f"candidato {_+1}°: ");
    lista_candidatos.append(candidatos)

votos = []    
for _ in range(n_candidatos):
    qtd_votos = int(input(f"quantidade de votos {lista_candidatos[_]}: "))
    votos.append(qtd_votos)

maior = votos[0]
for _ in range(n_candidatos):
    if votos[_] > maior:
        maior = votos[_]

empatados = []
for _ in range(n_candidatos):
    if votos[_] == maior:
        empatados.append(lista_candidatos[_])

if len(empatados) > 1:
    print(f"empate entre: {', '.join(empatados)} com {maior} votos cada")
else:
     print(f"vencedor: {empatados[0]} com {maior} votos")

"""
    
    
"""   
candidato_1 = input("nome do primiero candidato: ")
candidato_2 = input("nome do segundo candidato:  ")

votos_cand_1 = int(input(f"votos {candidato_1}: "))
votos_cand_2 = int(input(f"votos {candidato_2}: "))

#lista?
#laço

if votos_cand_1 > votos_cand_2:
    print(f"{candidato_1} e o vencedor")
elif votos_cand_2 > votos_cand_1:
    print(f"{candidato_2} e o vencedor")
elif votos_cand_1 == votos_cand_2 or votos_cand_2 == votos_cand_1:
    print("empate")
""" 
 
# questão 5
numero = int(input("numero: "))

if numero >= 1 and numero <=4:
    n =  (numero / 2)) +  (4 * numero) / 7
    print(n)
#elif numero >= 5 and numero <=9:
#    n = ()
    