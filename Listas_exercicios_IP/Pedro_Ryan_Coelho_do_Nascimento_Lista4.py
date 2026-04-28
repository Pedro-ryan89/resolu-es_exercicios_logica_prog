# ============================================================
# Lista de Exercícios 04 – Estruturas de Repetição
# IFCE – Tecnologia em Análise e Desenvolvimento de Sistemas
# ============================================================

# ======================== Questão 1 ========================
pares = 0
impares = 0
contador = 0

while contador < 10:
    numero = int(input(f"Digite o {contador + 1}º número: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    contador += 1

print(f"Pares: {pares}")
print(f"Ímpares: {impares}")

# ======================== Questão 2 ========================
trocou = False

while not trocou:
    senha_antiga = input("Digite sua senha antiga: ")
    senha_nova = input("Digite sua nova senha: ")
    confirmacao = input("Confirme sua nova senha: ")

    if senha_nova == senha_antiga:
        print("Erro: a nova senha deve ser diferente da antiga. Tente novamente.\n")
    elif senha_nova != confirmacao:
        print("Erro: a nova senha e a confirmação não coincidem. Tente novamente.\n")
    else:
        print("Senha trocada com sucesso!")
        trocou = True

# ======================== Questão 3 ========================
numero = int(input("Digite um número inteiro: "))

if numero <= 1:
    print(f"{numero} NÃO é primo.")
else:
    divisor = 2
    eh_primo = True

    while divisor * divisor <= numero:
        if numero % divisor == 0:
            eh_primo = False
            break
        divisor += 1

    if eh_primo:
        print(f"{numero} É primo.")
    else:
        print(f"{numero} NÃO é primo.")

# ======================== Questão 4 ========================
numero = int(input("Digite um número inteiro positivo: "))

fatorial = 1
i = 1

while i <= numero:
    fatorial *= i
    i += 1

print(f"O fatorial de {numero} é {fatorial}.")

# ======================== Questão 5 ========================
total_eleitores = int(input("Digite o número total de eleitores: "))

votos_1 = 0
votos_2 = 0
votos_3 = 0
eleitor = 1

while eleitor <= total_eleitores:
    print(f"\nEleitor {eleitor}:")
    print("Candidatos: 1, 2 ou 3")
    voto = int(input("Vote: "))

    if voto == 1:
        votos_1 += 1
    elif voto == 2:
        votos_2 += 1
    elif voto == 3:
        votos_3 += 1
    else:
        print("Voto inválido! Este voto será desconsiderado.")

    eleitor += 1

print("\n--- Resultado da Eleição ---")
print(f"Candidato 1: {votos_1} voto(s)")
print(f"Candidato 2: {votos_2} voto(s)")
print(f"Candidato 3: {votos_3} voto(s)")

# ======================== Questão 6 ========================
a = 1
b = 1

print("Série de Fibonacci (até > 500):")
print(a, end=" ")

while b <= 500:
    print(b, end=" ")
    a, b = b, a + b

print()

# ======================== Questão 7 ========================
# Número definido diretamente no código (sem import random)
numero_misterioso = 42
acertou = False

print("Adivinhe o número misterioso entre 1 e 100!")

while not acertou:
    tentativa = int(input("Sua tentativa: "))

    if tentativa < numero_misterioso:
        print("Muito baixo! Tente um número maior.")
    elif tentativa > numero_misterioso:
        print("Muito alto! Tente um número menor.")
    else:
        print(f"Parabéns! Você acertou! O número era {numero_misterioso}.")
        acertou = True

# ======================== Questão 8 ========================
numero = int(input("Digite um número inteiro positivo: "))

passos = 0
n = numero

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    passos += 1

print(f"O número {numero} chegou ao ciclo em {passos} passo(s).")

# ======================== Questão 9 ========================
numeros = [2, 4, 6, 8, 10]
soma = 0

for numero in numeros:
    soma += numero

print(f"Soma dos elementos: {soma}")

# ======================== Questão 10 ========================
palavra = input("Digite uma palavra: ")

for caractere in palavra:
    print(caractere)

# ======================== Questão 11 ========================
frase = input("Digite uma frase: ")
vogais = "aeiouAEIOU"
contagem = 0

for caractere in frase:
    if caractere in vogais:
        contagem += 1

print(f"Número de vogais: {contagem}")

# ======================== Questão 12 ========================
n = int(input("Quantos termos da série de Fibonacci deseja gerar? "))

a = 1
b = 1

print("Série de Fibonacci:")
for i in range(n):
    if i == 0:
        print(a, end=" ")
    elif i == 1:
        print(b, end=" ")
    else:
        proximo = a + b
        a = b
        b = proximo
        print(b, end=" ")

print()

# ======================== Questão 13 ========================
inicio = int(input("Digite o número inicial do intervalo: "))
fim = int(input("Digite o número final do intervalo: "))

print(f"Números primos entre {inicio} e {fim}:")

for numero in range(inicio, fim + 1):
    if numero <= 1:
        continue

    eh_primo = True
    for divisor in range(2, int(numero ** 0.5) + 1):
        if numero % divisor == 0:
            eh_primo = False
            break

    if eh_primo:
        print(numero, end=" ")

print()

# ======================== Questão 14 ========================
frase = input("Digite uma frase: ")
invertida = ""

for caractere in frase:
    invertida = caractere + invertida

print(f"Frase invertida: {invertida}")

# ======================== Questão 15 ========================
frase = input("Digite uma frase: ")
vogais_minusculas = "aeiou"
resultado = ""

for caractere in frase:
    if caractere in vogais_minusculas:
        resultado += "i"
    else:
        resultado += caractere

print(f"Na língua do i: {resultado}")

# ======================== Questão 16 ========================
n = int(input("Quantas linhas terá a árvore de natal? "))

for i in range(n):
    estrelas = 2 * i + 1
    espacos = n - i - 1
    print(" " * espacos + "*" * estrelas)

# ======================== Questão 17 ========================
numero = int(input("Montar a tabuada de: "))
inicio = int(input("Começar por: "))
fim = int(input("Terminar em: "))

for i in range(inicio, fim + 1):
    print(f"{numero} x {i} = {numero * i}")

# ======================== Questão 18 ========================
# 24h do jogo = 1h real → cada minuto do jogo = 2,5s reais
# Sem time.sleep, apenas exibimos todas as horas e minutos do dia

print("Relógio do IF Life (24h do jogo):")

for minuto_total in range(1440):
    horas = minuto_total // 60
    minutos = minuto_total % 60
    print(f"{horas:02d}:{minutos:02d}")