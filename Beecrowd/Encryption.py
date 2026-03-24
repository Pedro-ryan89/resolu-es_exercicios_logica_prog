n = int(input("numero de palavras:"))

for _ in range(n):
    letras_iniciais = input()
    resultado_primeiro_laco = ""

    #1 etapa: adicionar +3 em cada letra separadamente pra depois inverter 
    for letras in letras_iniciais:
        if letras.isalpha():
            primeiro_laco = chr(ord(letras) + 3)
            resultado_primeiro_laco += primeiro_laco
        else:
             resultado_primeiro_laco += letras

    #2 etapa: decobri essa função que faz a reversão da lista eu tentei outras formas mais complicou demais
    resultado_primeiro_laco = resultado_primeiro_laco[::-1]

    #3 etapa: demorei um pouco para entender que precisva dividir nao a string e sim tamanho dela
    metade = len(resultado_primeiro_laco) // 2 
    resultado_final = ""

    for i in range(len(resultado_primeiro_laco)):
        if i >= metade():
            resultado_final += ((chr(ord(resultado_primeiro_laco[i]) - 1)))
        else:
            resultado_final += resultado_primeiro_laco[i]

    print(resultado_final)
                 


