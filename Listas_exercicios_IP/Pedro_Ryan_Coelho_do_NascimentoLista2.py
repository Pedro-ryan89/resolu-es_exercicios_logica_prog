# Questão1

"""
atividade = int(input("insira um numero inteiro: "))
resultado = atividade**0.5
print(f"qualqeur coisa {resultado:.2f}")
"""
# Questão 2

"""
colonia = int(input("insira um numeroa: "))
hora = int(input("insira uma quantidade de horas: "))
resultado = colonia * hora**2
print(resultado)

"""

# Questão 3

"""

numero = float(input("insira um numero inteiro: "))
triplo_do_numero = 3 * numero 
setimo_do_numero = (2 * numero) / 7 
media = (triplo_do_numero + setimo_do_numero ) / 2 
quadruplo = 4 * media
resultado = quadruplo ** 2 

print(f"resultado = {resultado:.2f}")

"""

# Questão 4

"""
segundos = int(input("insira os segundos: "))
#dias = segundos // 86400               #fiquei curiso em relação ao calculo dos dias
#horas = (segundos % 86400) // 3600     # calculo considerando os dias
horas = segundos // 3600
minutos = (segundos % 3600) // 60
seg = segundos % 60

# aparentemente se quiser mostrar somente os especificos e so fazer uma checagem que evita mostrar todos de uma vez (1 dias 0 hr 0 min 0 seg) -> (1 dia) considerndo que temos o tratamento para isso semelhantes ao de baixo

#if dias > 0:
#    print(f"duração = {dias} dias {horas} hr {minutos} min {seg} seg")
#else:

print(f"duração = {horas} hr {minutos} min {seg} seg")
"""

# Questão 5

"""
altura = float(input("Digite a altura do prédio: "))
sombra = float(input("Digite o comprimento da sombra: "))


hipotenusa = (altura**2 + sombra**2) ** 0.5

seno = altura / hipotenusa
cosseno = sombra / hipotenusa

print(f"Seno: {seno:.2f}")
print(f"Cosseno: {cosseno:.2f}")

"""

# Questão 6

"""
#ideia semelhante a questão do tempo se fosse contando os centavos era trabalhando com os restos
valor_conta = float(input("valor da conta: "))

valor_amigo_pobre =  valor_conta % 47 

print(f"o amigo pobre pagara R${valor_amigo_pobre:.2f}") 
"""

# Questão 7

"""
nota_ava_1 = float(input("primeira avaliação: "))
nota_ava_2 = float(input("segunda avaliação: "))
nota_ava_3 = float(input("terceira avaliação: "))

media_ponderada = (nota_ava_1 * 2 + nota_ava_2 * 3 + nota_ava_3 * 5) / 10

print(f"Media Ponderada = {media_ponderada}")
"""

# Questão 8
"""

# print("insira os valores")
# a = int(input("valor a: "))
# b = int(input("valor b:"))
# c = int(input("valor c: "))
# d = int(input("valor d: "))
# e = int(input("valor e "))
# f = int(input("valor f: "))

#sempre tem uma forma mais inteligente de fazer.....
contador = 0
lista_valores = []

# lista_valores = [int(input("adicione os valores: ")) for _ in range(6)] <- bruxaria

while contador < 6:
    elementos = int(input("adicione os valores: "))
    lista_valores.append(elementos)
   
    contador += 1

a , b, c, d, e, f = lista_valores
resultado_X = (((c * e) - (b * f)) / ((a * e) - (b * d)))
resultado_Y = (((a * f) - (c * d)) / ((a * e) - (b * d)))

print(f"X: {resultado_X} e Y:{resultado_Y}")

"""

# Questão 9

"""
valor_da_conta = float(input("valor da conta: "))

wand = valor_da_conta // 3
wend = valor_da_conta // 3
wind = valor_da_conta // 3 + valor_da_conta % 3

print(f"wan = R${wand} - wen = R${wend} - win = R${wind}")

"""

# Questão 10

"""
calucula_nao_sei_oque = [float(input("adicione os valores: ")) for _ in range(4)]

x1, y1, x2, y2 = calucula_nao_sei_oque
calcula_distancia = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

print(f"A distância entre as duas cidade é{calcula_distancia}")

"""

# Questão 11

altura_edi = float(input("Altura do Edi (m): "))
sombra_edi = float(input("Sombra do Edi (m): "))
sombra_predio = float(input("Sombra do prédio (m): "))

altura_predio = (altura_edi * sombra_predio) / sombra_edi

print(f"Altura do prédio: {altura_predio:.2f} metros")





