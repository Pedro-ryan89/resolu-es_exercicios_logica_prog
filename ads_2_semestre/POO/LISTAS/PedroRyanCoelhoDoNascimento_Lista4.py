# ============================================================
# Lista de Exercícios 04 – Associação de Classes.
# IFCE - Tecnologia em Analise e Desenvolvimento de Sistemas
# ============================================================



# ======================== Questão 1 ========================


# class Pet:
#     def __init__(self,nome: str,caracteristica: str) -> None:
#         self.nome = nome
#         self.caracteristica = caracteristica 
    
#     def __str__(self) -> str:
#         return f"{self.nome}, a {self.caracteristica}"   
    
    
# class Person:
#     def __init__(self,nome: str,petpet) -> None:
#         self.nome = nome
#         self.pet = petpet
        
#     def __str__(self) -> str:
#         return f"{self.nome}, his Pet is {self.pet}"
    
    
# hulda = Pet("Hulda", "mixed breed")
# hesi = Person("Hesi", hulda)

# print(hesi)



# ======================== Questão 2 ========================



# class Present:
#     def __init__(self,name: str,weight: int) -> None:
#         self.name = name
#         self.weight = weight
        
        
#     def __str__(self) -> str:
#         return (
#             f"{self.name} ({self.weight}kg)"
#         )
        

# class Box:
#     def __init__(self) -> None:
#         self.present = []
        
        
#     def add_present(self,present: Present) -> None:
#         self.present.append(present)
        
#     def total_weight(self) -> int:
#         peso = 0
#         for presents in self.present:
#             peso += presents.weight
#         return peso
        
        

# book = Present("ABC Book", 2)

# box = Box()

# box.add_present(book)
# print(box.total_weight())

# cd = Present("Pink Floyd: Dark Side of the Moon", 1)
# box.add_present(cd)
# print(box.total_weight())



# ======================== Questão 3 ========================


# class Contato:
#     def __init__(self,nome: str,tell: str):
#         self.__nome = nome
#         self.__tell = tell
        
#     @property
#     def obter_contato(self) -> str:
#         return self.__nome
    
    
#     def __str__(self) -> str:
#         return f"{self.__nome} - {self.__tell}"

    
    
# class Agenda:
#     def __init__(self):
#         self.contatos = []
        
#     def adicionar_contato(self, contato: Contato) -> None:
#         self.contatos.append(contato)
#         self.contatos.sort(key=lambda contato: contato.obter_contato.lower())
        
        
#     def remover_contato(self,contato: Contato) -> None:
#         self.contatos.remove(contato)
            
#     def exibir_contatos(self) -> None:
#         for indice,contato in enumerate(self.contatos,start=1):
#             print(f"{indice}. {contato}")
            
            
# pedro = Contato("Pedro","12345678")
# chico = Contato("chico dede","12345678")
# sapao = Contato("sapao","12345678")

# agenda = Agenda()

# agenda.adicionar_contato(pedro)
# agenda.adicionar_contato(chico)
# agenda.adicionar_contato(sapao)

# agenda.exibir_contatos()

# print("\nREMOVENDO CONTATO\n")
# agenda.remover_contato(sapao)

# agenda.exibir_contatos()



# ======================== Questão 4 ========================

# import random

# class Carta:
#     def __init__(self,valor: int | str,naipe: str) -> None:
#         self.valor = valor
#         self.naipe = naipe
        
        
#     def __str__(self) -> str:
#         return f"{self.valor} - {self.naipe}"
        
        
        
# class Baralho:
#     valores = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
#     naipes = ["Paus", "Copas", "Espadas", "Ouros"]
    
#     def __init__(self) -> None:
#         self.cartas = []
        
#         for valor in self.valores:
#             for naipe in self.naipes:
#                 self.cartas.append(Carta(valor,naipe))
                
#     def embaralhar(self) -> None:
#         random.shuffle(self.cartas)
    
    
#     def dar_carta(self) -> Carta:
#        return self.cartas.pop()
        
        
# baralho = Baralho()

# # Testar criação
# print("Quantidade inicial:", len(baralho.cartas))
# print("Primeira carta:", baralho.cartas[-1])

# # Testar embaralhamento
# baralho.embaralhar()
# print("Após embaralhar:", baralho.cartas[-1])

# # Testar retirada de carta
# carta = baralho.dar_carta()
# print("Carta retirada:", carta)
# print("Cartas restantes:", len(baralho.cartas))


# ======================== Questão 5 ========================


# class Aluno:
#     def __init__(self,nome: str,idade: int,nota: float) -> None:
#         self.__nome = nome
#         self.__idade = idade
#         self.__nota = nota
        
#     @property
#     def nome(self):
#         return self.__nome
    
#     @nome.setter
#     def nome(self, nome_aluno: str) -> None:
#         self.__nome = nome_aluno
        
#     @property
#     def idade(self):
#         return self.__idade
    
#     @idade.setter
#     def idade(self,idade_aluno: int) -> None:
#         self.__idade = idade_aluno
    
#     @property
#     def nota(self):
#         return self.__nota
    
#     @nota.setter
#     def nota(self,nota_aluno: int):
#         self.__nota = nota_aluno 
                
    
#     def __str__(self) -> str:
#         return f"nome: {self.__nome} | idade: {self.__idade} | nota: {self.__nota}"
    
# class Turma:
#     def __init__(self) -> None:
#         self.alunos = []
        
        
#     def adicionar_aluno(self,aluno: Aluno) -> None:
#         self.alunos.append(aluno)
#         self.alunos.sort(key=lambda aluno: aluno.nome.lower())
        
#     def remover_aluno(self,nome: str) -> None:
#         for aluno in self.alunos:
#             if aluno.nome == nome:
#                 self.alunos.remove(aluno)
#                 print(f"\naluno {aluno.nome} removido\n")
#                 break
        
#     def listar_alunos(self) -> None:
#         for indice,aluno in enumerate(self.alunos,start=1):
#             print(f"{indice}. {aluno}")
    

# pedro = Aluno("pedro",21,8)
# joao = Aluno("joao",19,9)
# julia = Aluno("julia",20,7)
# chico_dede = Aluno("chico dede",32,10)
# tecalandia = Aluno("tecalandia",30,10)
# sapao = Aluno("sapao",30,8)

# turma = Turma()

# turma.adicionar_aluno(pedro)
# turma.adicionar_aluno(joao)
# turma.adicionar_aluno(julia)
# turma.adicionar_aluno(chico_dede)
# turma.adicionar_aluno(tecalandia)
# turma.adicionar_aluno(sapao)

# print("\n-----LISTA ALUNOS-----\n")
# turma.listar_alunos()
# print("\n---------------------------")
# turma.listar_alunos()
# turma.remover_aluno("joao")


        
# ======================== Questão 6 ========================

# class Produto:
#     def __init__(self,codigo: int,nome: str,preco: int,quantidade: int) -> None:
#         self.codigo = codigo
#         self.nome = nome
#         self.preco = preco
#         self.quantidade = quantidade
        
    
#     def __str__(self) -> str:
#         return(
#             f"Produto: {self.nome} | codigo: {self.codigo} | quantidade: {self.quantidade} | preco: {self.preco}"
#         )

# class Estoque:
#     def __init__(self) -> None:
#         self.produtos: list[Produto] = []
        
        
#     def adicionar_produto(self,produto: Produto):
#         self.produtos.append(produto)
        
    
#     def remover_produto(self,codigo: int):
#         for cod in self.produtos:
#             if cod.codigo == codigo:
#                 self.produtos.remove(cod)
#                 print(f"\nproduto {cod.nome} removido\n")
#             else:
#                 print("produto nao encontrado")
#                 break
            
                        
#     def listar_produtos(self):
#         for indice,produto in enumerate(self.produtos, start=1):
#             print(f"{indice}. {produto}")
            

# estoque = Estoque()

# p1 = Produto(1, "Teclado", 100, 10)
# p2 = Produto(2, "Mouse", 50, 20)

# estoque.adicionar_produto(p1)
# estoque.adicionar_produto(p2)

# estoque.listar_produtos()
# # estoque.remover_produto(1)
# # estoque.listar_produtos()
            
# # ======================== Questão 7 ========================

# import os

# class Produto:
#     def __init__(self, codigo: int, valor: float, descricao: str) -> None:
#         self.__codigo = codigo
#         self.__valor = valor
#         self.__descricao = descricao

#     @property
#     def valor_produto(self) -> float:
#         return self.__valor

#     @property
#     def codigo_produto(self) -> int:
#         return self.__codigo

#     @property
#     def descricao(self) -> str:
#         return self.__descricao
    
    
#     def __str__(self) -> str:
#         return (
#             f"Código: {self.__codigo} | "
#             f"Valor: R$ {self.__valor:.2f} | "
#             f"Descrição: {self.__descricao}"
#         )

# class ItemPedido:
#     def __init__(self, produto: Produto, quantidade: int) -> None:
#         self.produto = produto
#         self.quantidade = quantidade
#         self.preco_unitario = produto.valor_produto
        
        
#     @property
#     def subtotal(self) -> float:
#         return self.quantidade * self.preco_unitario

#     def __str__(self) -> str:
#         return (
#             f"Produto: {self.produto.descricao}\n"
#             f"Preço unitário: R$ {self.preco_unitario:.2f}\n"
#             f"Quantidade: {self.quantidade}\n"
#             f"Subtotal: R$ {self.subtotal:.2f}"
#         )

# class Pedido:
#     def __init__(self) -> None:
#         self.itens: list[ItemPedido] = []

#     def adicionar_itens(self, item: ItemPedido) -> None:
#         self.itens.append(item)

#     def obter_total(self) -> float:
#         total = 0.0

#         for item in self.itens:
#             total += item.subtotal
#         return total

#     def imprimir_pedido_completo(self) -> None:
#         for item in self.itens:
#             print(item)

#         print(f"Total: R$ {self.obter_total():.2f}")


# def listar_produtos(produtos: list[Produto]) -> None:
#     if not produtos:
#         print("Nenhum produto cadastrado.")
#         return

#     for produto in produtos:
#         print(produto)
        
        
# def adicionar_item_ao_pedido(produtos: list[Produto], pedido: Pedido) -> None:
#     if not produtos:
#         print("\nCadastre pelo menos um produto primeiro.")
#     else:
#         listar_produtos(produtos)

#         try:
#             codigo = int(input("\nCódigo do produto: "))
#             produto_escolhido = buscar_produto(produtos, codigo)

#             if produto_escolhido is None:
#                 print("\nProduto não encontrado.")
#             else:
#                 quantidade = int(input("Quantidade: "))

#                 if quantidade <= 0:
#                     print("\nA quantidade deve ser maior que zero.")
#                 else:
#                     item = ItemPedido(produto_escolhido, quantidade)
#                     pedido.adicionar_itens(item)
#                     print("\nItem adicionado ao pedido!")

#         except ValueError as error:
#             print(f"\nErro: {error}")
        
# def buscar_produto(produtos: list[Produto],codigo:int) -> Produto | None:
#     produto_escolhido = None

#     for produto in produtos:
#         if produto.codigo_produto == codigo:
#             produto_escolhido = produto
#             break
        
#     return produto_escolhido


# def menu() -> None:
#     produtos: list[Produto] = []
#     pedido = Pedido()

#     while True:
#         os.system("cls" if os.name == "nt" else "clear")

#         print("===== SISTEMA DE PEDIDOS =====")
#         print("1 - Cadastrar produto")
#         print("2 - Criar novo pedido")
#         print("3 - Adicionar item ao pedido")
#         print("4 - Imprimir pedido completo")
#         print("5 - Listar produtos")
#         print("6 - Sair")

#         opcao = input("\nEscolha uma opção: ")

#         match opcao:
#             case "1":
#                 try:
#                     codigo = int(input("Código do produto: "))
#                     descricao = input("Descrição: ")
#                     valor = float(input("Preço: R$ ").replace(",", "."))

#                     produto = Produto(codigo, valor, descricao)
#                     produtos.append(produto)

#                     print("\nProduto cadastrado com sucesso!")

#                 except ValueError as error:
#                     print(f"\nErro: {error}")

#             case "2":
#                 pedido = Pedido()
#                 print("\nNovo pedido criado!")

#             case "3":
#                 if not produtos:
#                     print("\nCadastre pelo menos um produto primeiro.")
#                 else:
#                     listar_produtos(produtos)
#             case "4":
#                 print("\n===== PEDIDO COMPLETO =====")

#                 if not pedido.itens:
#                     print("O pedido ainda não possui itens.")
#                 else:
#                     pedido.imprimir_pedido_completo()

#             case "5":
#                 print("\n===== PRODUTOS CADASTRADOS =====")
#                 listar_produtos(produtos)

#             case "6":
#                 print("\nEncerrando o sistema...")
#                 break

#             case _:
#                 print("\nOpção inválida!")

#         input("\nPressione ENTER para continuar...")


# menu()


# ======================== Questão 8 ========================

import random
import os
import time
class Carro:
    def __init__(self,nome) -> None:
        self.nome = nome
        self.posicao = 0
        self.velocida = 0
    
    def acelerar(self):
       self.velocidade = random.randint(1,5)
       self.posicao += self.velocidade
       
       
    def __str__(self) -> str:
        return f"{self.nome}: {'#' * self.posicao}"
    

carros = [
    Carro("Carro 1"),
    Carro("Carro 2"),
    Carro("Carro 3"),
    Carro("Carro 4")
]


def iniciar_corrida(tamanho_pista: int):
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        for carro in carros:
            carro.acelerar()
            print(carro)

            if carro.posicao >= tamanho_pista:
                print(f"\nVencedor: {carro.nome}!")
                return

        time.sleep(0.5)
            
        
    
iniciar_corrida(100)