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