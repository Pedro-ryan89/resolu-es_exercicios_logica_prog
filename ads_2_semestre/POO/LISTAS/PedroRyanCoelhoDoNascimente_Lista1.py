# ============================================================
# Lista de Exercícios 01 - CLASSE
# IFCE - Tecnologia em Analise e Desenvolvimento de Sistemas
# ============================================================


# ======================== Questão 1-2-3 ========================


# class Livro:
#     def __init__(self, nome: str, autor: str, genero: str, ano: int):
#         self.nome = nome
#         self.autor = autor
#         self.genero = genero
#         self.ano = ano


# def livro_mais_antigo(livro1: Livro, livro2: Livro):
#     if livro1.ano <= livro2.ano:
#         return livro1.nome
#     else:
#         return livro2.nome


# def livro_do_genero(livros: list, genero: str):
#     livros_mesmo_genero = []

#     for livro in livros:
#         if livro.genero == genero:
#             livros_mesmo_genero.append(livro)

#     for livro in livros_mesmo_genero:
#         print(livro.nome)


# dom_casmurro = Livro("Dom Casmurro", "Machado de Assis", "romance", 1899)
# o_hobbit = Livro("O Hobbit", "J.R.R. Tolkien", "fantasia", 1937)
# print(f"{dom_casmurro.autor}: {dom_casmurro.nome} ({dom_casmurro.ano})")
# print(f"O gênero do livro {o_hobbit.nome} é {o_hobbit.genero}")
# print(livro_mais_antigo(dom_casmurro, o_hobbit))
# livros = [dom_casmurro, o_hobbit]
# livro_do_genero(livros, "fantasia")


# ======================== Questão 4 ========================


# class Pessoa:
#     def __init__(self, nome: str):
#         self.nome = nome


# def retorna_primeiro_nome(self):
#     primeiro_nome = self.nome.split()
#     return primeiro_nome[0]


# def retorna_segundo_nome(self):
#     segundo_nome = self.nome.split()
#     return segundo_nome[1]


# nome = input("digite nome: ")

# pessoa = Pessoa(nome)

# print(retorna_primeiro_nome(pessoa))
# print(retorna_segundo_nome(pessoa))


# ======================== Questão 5 ========================


class Carro:
    def __init__(
        self, marca: str, modelo: str, ano: int, cor: str, velociada_atual: int
    ) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade_atual = velociada_atual

    def acelerar(self):
        self.velocidade_atual += 10

    def frear(self):
        if self.velocidade_atual <= 0:
            print("nao e possivel diminuir velocidade")
        else:
            self.velocidade_atual -= 10

    def pintar(self, nova_cor):
        self.cor = nova_cor

    def mostrar_informacoes(self):
        print(
            f"marca: {self.marca}\nmodelo: {self.modelo}\nano: {self.ano}\ncor: {self.cor}\nvelocidade: {self.velocidade_atual}"
        )


carro = Carro("carro", "carro teste", 2005, "amarelo", 60)
carro.acelerar()
carro.frear()
carro.pintar("vermelho")
carro.mostrar_informacoes()
