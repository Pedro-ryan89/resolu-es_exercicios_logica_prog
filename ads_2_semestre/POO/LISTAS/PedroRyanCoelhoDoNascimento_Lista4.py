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


