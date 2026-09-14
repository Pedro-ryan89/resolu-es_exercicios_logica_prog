#1º QUESTÃO: Escreva a Classe Livro, com os atributos nome, autor, gênero e ano e com o construtor 
# que assinala os valores iniciais destes atributos.

class Livro:
    def __init__(self, nome, autor, genero, ano):
        self.nome = nome
        self.autor = autor
        self.genero = genero
        self.ano = ano

dom_casmurro = Livro("Dom Casmurro", "Machado de Assis", "romance", 1899)
o_hobbit = Livro("O Hobbit", "J.R.R Tolkien", "fantasia", 1937)

print(f"{dom_casmurro.autor}: {dom_casmurro.nome} ({dom_casmurro.ano})")
print(f"O gênero do livro {o_hobbit.nome} é {o_hobbit.genero}")
print(" ")

#2º QUESTÃO: Crie uma função nomeada de livro_mais_antigo(livro1: Livro, livro2: Livro) que 
# recebe dois objetos do tipo livro como argumento e que imprime uma mensagem informando os 
# detalhes do livro mais antigo. Caso ambos forem escritos no mesmo ano, isto deve ser informado. 
# Teste a função criada.

class Livro:
    def __init__(self, nome, autor, genero, ano:int):
        self.nome = nome
        self.autor = autor
        self.genero = genero
        self.ano = ano
def livro_mais_antigo(livro1: Livro, livro2: Livro):
    if (livro1.ano < livro2.ano):
        print(f"{livro1.autor}: {livro1.nome}, {livro1.genero} ({livro1.ano})")
    elif(livro2.ano < livro1.ano):
        print(f"{livro2.autor}: {livro2.nome}, {livro2.genero} ({livro2.ano})")
    else:
        print("Os 2 livros foram publicado no mesmo ano.")

ready_player_one = Livro("Ready Player One", "Ernest Cline", "Sci-Fi", 2011)
the_hunter_games = Livro("The Hunter Games", "Suzanne Collins", "Sci-Fi", 2011)
five_nights_at_freddys = Livro("Five Nights at Freddy's: The Silver Eyes", "Scott Cawthon", "Sci-Fi", 2015)
insomnia = Livro("Insomnia", "Stephen King", "Horror", 1994)

livro_mais_antigo(ready_player_one, the_hunter_games)
livro_mais_antigo(insomnia, five_nights_at_freddys)
livro_mais_antigo(five_nights_at_freddys, ready_player_one)
print(" ")

#3º QUESTÃO: Crie uma função nomeada livros_do_genero(livros: List, genero: str) que recebe como 
# argumentos uma lista de objetos do tipo livro e uma string que representa o gênero. Esta função
# deve retornar uma nova lista que contêm apenas livros da lista recebida cujo gênero é igual ao 
# passado como argumento. Teste a função criada.

class Livro:
    def __init__(self, nome, genero):
        self.nome = nome
        self.genero = genero
def lista_generos(lista:list, genero:str):
    nova_lista = []
    for livro in lista:
        if (livro.genero == genero):
            nova_lista.append(livro)
    if(len(nova_lista) == 0):
        print("Não há livros desse gênero no catálogo.")
    else:
        for livro in nova_lista:
            print(livro.nome)

ready_player_one = Livro("Ready Player One", "SCI-FI")
the_hunter_games = Livro("The Hunter Games", "SCI-FI")
insomnia = Livro("Insomnia - The Night Walkers #1", "HORROR")
paranoia = Livro("Paranoia - The Night Walkers #2", "HORROR")
mania = Livro ("Mania - The Night Walkers #3", "HORROR")
harry_potter1 = Livro("Harry Potter and the Philosopher's Stone", "FANTASIA")
harry_potter2 = Livro ("Harry Potter and the Chamber of Secrets", "FANTASIA")
harry_potter3 = Livro ("Harry Potter and the Prisoner of Azkaban", "FANTASIA")
harry_potter4 = Livro ("Harry Potter and the Goblet of Fire", "FANTASIA")
livros = [ready_player_one, the_hunter_games, insomnia, paranoia, mania,harry_potter1,harry_potter2,harry_potter3,harry_potter4]

while True:
    escolha = input("Qual gênero de livros gostaria de encontrar? \n").upper()
    lista_generos(livros, escolha)
    escolha = input("Você gostaria de continuar procurando? (SIM OU NÃO) \n").upper()
    if(escolha == "SIM"):
        continue;
    else:
        break;
print(" ")

#4º QUESTÃO: Escreva uma classe chamada Pessoa com um único atributo chamado nome, que deve ser 
# definido por meio de um argumento passado ao construtor.

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def retorna_primeiro_nome(self):
        return self.nome.split(" ")[0]
    
    def retorna_ultimo_nome(self):
        return self.nome.split(" ")[1]
    
daniel = Pessoa("Daniel Araújo")

print(daniel.retorna_primeiro_nome())
print(daniel.retorna_ultimo_nome())
print(" ")

#5º QUESTÃO: Classe Carro: Crie uma classe que modele um carro:

import random
class Carro:
    def __init__(self, marca, modelo, ano, cor, velocidade_atual):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade_atual = velocidade_atual
    def acelerar(self):
        self.velocidade_atual += 10
    def frear (self):
        if(self.velocidade_atual <= 10):
            self.velocidade_atual = 0
        else:
            self.velocidade_atual -= 10
    def pintar(self):
        cores = ["Preto", "Branco", "Prata", "Cinza", "Vermelho", "Azul", "Marrom", "Verde", "Amarelo", "Laranja"]
        nova_cor = cores[random.randint(0, 9)]
        while(nova_cor == self.cor):
            nova_cor = cores[random.randint(0, 9)]
        self.cor = nova_cor
        print(f"A nova cor do seu carro é: {nova_cor}")
    def mostrar_informacoes (self):
        print(f"A marca é {self.marca}, modelo {self.modelo}, ano {self.ano}, da cor {self.cor}, com velocidade atual de {self.velocidade_atual}km/h")

marca = input("Qual a marca do seu carro? \n")
modelo = input("Qual o modelo do seu carro? \n")
ano = input("Qual o ano do seu carro? \n")
cor = input("Qual a cor do seu carro? \n")
try:
    velocidade_atual = int(input("Qual a velocidade atual do seu carro? \n"))
except:
    print("Dê uma resposta váida.")

carro_motorista = Carro(marca, modelo, ano, cor, velocidade_atual)

while True:
    while True:
        try:
            print("1 - ACELERAR      2 - FREAR")
            print("3 - PINTAR        4 - MOSTRAR INFORMAÇÕES")
            print("       5 - SAIR DO CARRO       ")
            print(" ")
            escolha = int(input("O que você gostaria de fazer? \n"))
            if (1<=escolha<=5):
                break;
            else:
                print("Escolha uma opção válida.")
                print(" ")
        except ValueError:
            print("Forma de resposta inválida.")
            print(" ")
    if(escolha == 1):
        carro_motorista.acelerar()
        print(" ")
    elif(escolha == 2):
        if(carro_motorista.velocidade_atual == 0):
            print("Seu carro já está parado. \n")
        else:
            carro_motorista.frear()
        print(" ")
    elif(escolha == 3):
        carro_motorista.pintar()
        print(" ")
    elif(escolha == 4):
        carro_motorista.mostrar_informacoes()
        print(" ")
    elif(escolha == 5):
        if(carro_motorista.velocidade_atual > 0):
            print("Está tentando se matar? O carro ainda está em movimento!")
            print(" ")
        else:
            print("Você saiu com sucesso e em segurança de seu carro.")
            break;