#Sobrescreve o arquivo
with open("Ativ_01_03.txt", "w", encoding="utf-8") as arq:
    arq.write("Relatorio da turma \n")
    arq.write("Media geral: 7.4 \n")

#Adiciona uma nova linha
with open("Ativ_01_03.txt", "a", encoding="utf-8") as arq:
    arq.write("Situacao: Turma aprovada \n")