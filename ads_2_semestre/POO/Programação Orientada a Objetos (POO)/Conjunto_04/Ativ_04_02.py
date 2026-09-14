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