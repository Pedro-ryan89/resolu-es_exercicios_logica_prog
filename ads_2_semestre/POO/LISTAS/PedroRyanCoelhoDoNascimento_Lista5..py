
# ============================================================
# Lista de Exercícios 05 – Herança.
# IFCE - Tecnologia em Análise e Desenvolvimento de Sistemas
# ============================================================



# ======================== Questão 1 ========================
# especialização de um classe Pessoa.
# ============================================================


# class Pessoa:
#     def __init__(self, nome: str, idade: int) -> None:
#         self.nome = nome
#         self.idade = idade
    
#     def apresentar_detalhes(self) -> str:
#         return f"Nome: {self.nome} - Idade: {self.idade}"
 
# class Aluno(Pessoa):
#     def __init__(self,nome: str,idade: int,matricula: str) -> None:
#         super().__init__(nome,idade)
#         self.matricula = matricula
        
#     def apresentar_detalhes(self) -> str:
#         return f"{super().apresentar_detalhes()} - Matricula: {self.matricula}"
    

# aluno = Aluno("Ana", 20, "2026001")
# print(aluno.apresentar_detalhes()) # Nome: Ana - idade: 20 - Matrícula: 2026001


# ======================== Questão 2 ========================
# polimorfismo com funcionarios.
# ============================================================

# class Funcionario:
#     def __init__(self,nome:str) -> None:
#         self.nome = nome
        
#     def calcular_pagamento(self) -> int:
#         return 1615


# class FuncionarioHorista(Funcionario):
#     def __init__(self,nome:str ,horas: int, valor_hora: int) -> None:
#         super().__init__(nome)
#         self.horas = horas
#         self.valor_hora= valor_hora
    
#     def calcular_pagamento(self) -> int:
#         return  self.horas * self.valor_hora
    
    
# class FuncionarioComissionado(Funcionario):
#     def __init__(self, nome: str,comissao:  int) -> None:
#         super().__init__(nome)
#         self.comissao = comissao
        
#     def calcular_pagamento(self) -> int:
#         return (super().calcular_pagamento() + self.comissao)
    
    
# funcionarios = [
#     FuncionarioHorista("chico dede",40,7),
#     FuncionarioComissionado("pedro",900),
#     FuncionarioHorista("matheus",40,15),
#     Funcionario("sapao")
# ]   
    
# def salario_funcionarios(funcionarios: list[Funcionario]):
#     for funcionario in funcionarios:
#         print (f"{funcionario.nome}: {funcionario.calcular_pagamento()}")
        
# salario_funcionarios(funcionarios)

# ======================== Questão 3 ========================
# Especialize uma classe Pessoa utilizando herança.
# ============================================================

# class Pessoa():
#     def __init__(self,nome: str,cpf: str) -> None:
#         self.nome = nome
#         self.cpf = cpf

#     def apresentar(self) -> str:
#         return f"Nome: {self.nome} | CPF: {self.cpf}"
    
# class Servidor(Pessoa):
#     def __init__(self, nome: str, cpf: str,siape: int) -> None:
#         super().__init__(nome, cpf)
#         self.siape = siape
        
#     def apresentar(self) -> str:
#         return f"{super().apresentar()} | Siape: {self.siape}"

# class Professor(Servidor):
#     def __init__(self, nome: str, cpf: str, siape: int,disciplinas: list[Disciplina]) -> None:
#         super().__init__(nome, cpf, siape)
#         self.disciplinas = disciplinas
        
#     def apresentar(self) -> str:
#         return f"{super().apresentar()} | disciplinas: {self.disciplinas}"

# class TAE(Servidor):
#     def __init__(self, nome: str, cpf: str, siape: int,funcao: str) -> None:
#         super().__init__(nome, cpf, siape)
#         self.funcao = funcao
        
#     def apresentar(self) -> str:
#         return f"{super().apresentar()} | Funcao: {self.funcao}"
    
# class Aluno(Pessoa):
#     def __init__(self, nome: str, cpf: str,matricula: int,curso: str,disciplinas: list[Disciplina]) -> None:
#         super().__init__(nome, cpf)
#         self.matricula = matricula
#         self.curso = curso
#         self.disciplinas = disciplinas
        
#     def apresentar(self) -> str:
#         return f"{super().apresentar()} | matricula: {self.matricula} | Curso: {self.curso} | Disciplinas: {self.disciplinas}"
        
        
# class Disciplina():
#     def __init__(self,nome: str,CH:int) -> None:
#         self.nome = nome
#         self.CH = CH
        
#     def __str__(self) -> str:
#         return f"{self.nome} - {self.CH} horas"
    
#     def __repr__(self) -> str:
#         return f"{self.nome} - {self.CH} horas"


# python = Disciplina("Python", 80)
# poo = Disciplina("POO", 60)
# redes = Disciplina("Redes", 80)
  
# pessoas = [
#     Pessoa("Pedro", "123"),
#     Servidor("Carlos", "456", 789),
#     Professor("Ana", "111", 222, [python, poo]),
#     TAE("Marcos", "333", 444, "Técnico de laboratório"),
#     Aluno("João", "555", 666, "ADS", [poo, redes])
# ]     

# def apresentar(pessoas: list[Pessoa]):
#     for indice,pessoa in enumerate(pessoas,start=1):
#         print(f"{indice} - {pessoa.apresentar()}")

# apresentar(pessoas)



# ======================== Questão 4 ========================
# Laptop e computador.
# ===========================================================

# class Computer():
#     def __init__(self,model: str,speed: int) -> None:
#         self.model = model
#         self.speed = speed
# class Laptop(Computer):
#     def __init__(self,model: str,speed: int,weight: int) -> None:
#         super().__init__(model,speed)
#         self.__weight = weight
        
#     @property
#     def weight(self):
#         return self.__weight
    
#     def __str__(self) -> str:
#         return f"{self.model} , {self.speed} MHz , {self.weight} Kg"
    
# laptop = Laptop("Notebook Pro",1500,2)
# print(laptop)
    


# ======================== Questão 5 ========================
# retangulo.
# ===========================================================

# class Rectangle():
#     def __init__(self,width: int,height: int) -> None:
#         self.widht = width
#         self.height = height
        
#     def area(self) -> int:
#         return self.height * self.widht
    
    
#     def __str__(self) -> str:
#         return f"area: {self.area()}"
        
# class Square(Rectangle):
#     def __init__(self, side: int) -> None:
#         super().__init__(side, side)
        
        
# rectangle = Rectangle(10, 5)
# square = Square(5)

# print(rectangle)
# print(square)

# ======================== Questão 6 ========================
# Pagamentos com herança e polimorfismo.
# ===========================================================

# from abc import ABC, abstractmethod

# class Pagamento(ABC):
#     def __init__(self,valor:int,tipo:str) -> None:
#         self.valor = valor
#         self.tipo = tipo
       
#     @abstractmethod 
#     def processar(self) -> str :
#         pass

# class PagamentoPix(Pagamento):
#     def __init__(self, valor: int, tipo: str) -> None:
#         super().__init__(valor, tipo)
        
#     def processar(self) -> str:
#         return f"pagamento: {self.tipo}  | no valor de {self.valor} aceito"
    

# class PagamentoCartao(Pagamento):
#     def __init__(self, valor: int, tipo: str,parcelas: str) -> None:
#         super().__init__(valor, tipo)
#         self.parcelas = parcelas
        
#     def processar(self) -> str:
#         return f"pagamento: {self.tipo}  | no valor de {self.valor} aceito | parcelado em {self.parcelas}"   
    
    
    
# carrinho = [
#     PagamentoPix(80,"pix"),
#     PagamentoCartao(80,"cartao","a vista")
# ]

# def processarpagamentos(carrinho: list[Pagamento]):
#     for pagamento in carrinho:
#         print(pagamento.processar())
    
# processarpagamentos(carrinho)
    
# ======================== Questão 7 ========================
#
# ===========================================================

# from abc import ABC, abstractmethod
# class CartaoMensagem(ABC):
#     def __init__(self,destinatario: str,remetente: str) -> None:
#         self.destinatario = destinatario
#         self.remetente = remetente
    
#     @abstractmethod
#     def retornar_mensagem(self) -> str:
#         pass
    
# class DiaDosNamorados(CartaoMensagem):

#     def retornar_mensagem(self) -> str:
#         return (
#             f"feliz dia dos namorados {self.destinatario}!, com carinho {self.remetente}"
#         )
    
# class Natal(CartaoMensagem):
        
#     def retornar_mensagem(self) -> str:
#         return (
#             f"feliz Natal {self.destinatario}!, com carinho {self.remetente}"
#         )
    
# class Aniversario(CartaoMensagem):
    
#     def retornar_mensagem(self) -> str:
#         return (
#             f"feliz Aniversario {self.destinatario}!, com carinho {self.remetente}"
#         )        

# destinatario = input("nome destinatario: ")
# remetente = input("nome remetente: ")


# cartoes = [
#     DiaDosNamorados(destinatario,remetente),
#     Natal(destinatario,remetente),
#     Aniversario(destinatario,remetente),
# ]

# def MostrarMensagens(cartoes: list[CartaoMensagem]):
#     for mensagem in cartoes:
#         print(mensagem.retornar_mensagem())
        
# MostrarMensagens(cartoes)

# ======================== Questão 8 ========================
# 
# ===========================================================





