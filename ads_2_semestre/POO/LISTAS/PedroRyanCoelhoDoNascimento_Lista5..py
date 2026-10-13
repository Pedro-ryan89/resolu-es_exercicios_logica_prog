
# ============================================================
# Lista de Exercícios 05 – Herança.
# IFCE - Tecnologia em Análise e Desenvolvimento de Sistemas
# ============================================================


# ======================== Questão 3 ========================
# Especialize uma classe Pessoa utilizando herança.
# ============================================================

# class Pessoa:
#     def __init__(self, nome: str, idade: int) -> None:
#         self.nome = nome
#         self.idade = idade
#
#     def apresentar_detalhes(self) -> str:
#         return f"Nome: {self.nome} - idade: {self.idade}"
#
#
# class Aluno(Pessoa):
#     def __init__(
#         self, nome: str, idade: int, matricula: str
#     ) -> None:
#         super().__init__(nome, idade)
#         self.matricula = matricula
#
#     def apresentar_detalhes(self) -> str:
#         detalhes = super().apresentar_detalhes()
#         return f"{detalhes} - Matrícula: {self.matricula}"
#
#
# aluno = Aluno("Ana", 20, "2026001")
# print(aluno.apresentar_detalhes())


# ======================== Questão 4 ========================
# Funcionários: herança e polimorfismo.
# ============================================================

# class Funcionario:
#     def __init__(self, nome: str) -> None:
#         self.nome = nome
#
#     def calcular_pagamento(self) -> float:
#         # Salário mínimo adotado como valor fixo de referência.
#         return 1621.00
#
#
# class FuncionarioHorista(Funcionario):
#     def __init__(
#         self, nome: str, horas: float, valor_hora: float
#     ) -> None:
#         super().__init__(nome)
#         self.horas = horas
#         self.valor_hora = valor_hora
#
#     def calcular_pagamento(self) -> float:
#         return self.horas * self.valor_hora
#
#
# class FuncionarioComissionado(Funcionario):
#     def __init__(
#         self, nome: str, comissao: float
#     ) -> None:
#         super().__init__(nome)
#         self.comissao = comissao
#
#     def calcular_pagamento(self) -> float:
#         return super().calcular_pagamento() + self.comissao
#
#
# def imprimir_pagamentos(funcionarios: list) -> None:
#     for funcionario in funcionarios:
#         pagamento = funcionario.calcular_pagamento()
#         print(
#             f"{funcionario.nome}: R$ {pagamento:.2f}"
#         )
#
#
# funcionarios = [
#     Funcionario("Carlos"),
#     FuncionarioHorista("Ana", 100, 20.00),
#     FuncionarioComissionado("Pedro", 500.00)
# ]
#
# imprimir_pagamentos(funcionarios)


# ======================== Questão 5 ========================
# Hierarquia de Pessoas.
# ============================================================

# class Pessoa:
#     def __init__(self, nome: str, cpf: str) -> None:
#         self.nome = nome
#         self.cpf = cpf
#
#
# class Servidor(Pessoa):
#     def __init__(
#         self, nome: str, cpf: str, codigo_siape: str
#     ) -> None:
#         super().__init__(nome, cpf)
#         self.codigo_siape = codigo_siape
#
#
# class Professor(Servidor):
#     def __init__(
#         self,
#         nome: str,
#         cpf: str,
#         codigo_siape: str,
#         disciplinas: list
#     ) -> None:
#         super().__init__(nome, cpf, codigo_siape)
#         self.disciplinas = disciplinas
#
#
# class TAE(Servidor):
#     def __init__(
#         self,
#         nome: str,
#         cpf: str,
#         codigo_siape: str,
#         funcao: str
#     ) -> None:
#         super().__init__(nome, cpf, codigo_siape)
#         self.funcao = funcao
#
#
# class Disciplina:
#     def __init__(self, nome: str, ch: int) -> None:
#         self.nome = nome
#         self.ch = ch
#
#     def __str__(self) -> str:
#         return f"{self.nome} - CH: {self.ch} horas"
#
#
# class Aluno(Pessoa):
#     def __init__(
#         self,
#         nome: str,
#         cpf: str,
#         matricula: str,
#         curso: str,
#         disciplinas: list
#     ) -> None:
#         super().__init__(nome, cpf)
#         self.matricula = matricula
#         self.curso = curso
#         self.disciplinas = disciplinas
#
#
# # Testes da hierarquia.
# poo = Disciplina("Programação Orientada a Objetos", 80)
# banco_dados = Disciplina("Banco de Dados", 60)
#
# professor = Professor(
#     "Maria",
#     "11111111111",
#     "SIAPE001",
#     [poo, banco_dados]
# )
#
# servidor_tae = TAE(
#     "João",
#     "22222222222",
#     "SIAPE002",
#     "Técnico de Laboratório"
# )
#
# aluno = Aluno(
#     "Ana",
#     "33333333333",
#     "2026001",
#     "Análise e Desenvolvimento de Sistemas",
#     [poo, banco_dados]
# )
#
# print(f"Professor: {professor.nome}")
# print(f"SIAPE: {professor.codigo_siape}")
# print("Disciplinas do professor:")
# for disciplina in professor.disciplinas:
#     print(disciplina)
#
# print(f"\nTAE: {servidor_tae.nome}")
# print(f"Função: {servidor_tae.funcao}")
#
# print(f"\nAluno: {aluno.nome}")
# print(f"Matrícula: {aluno.matricula}")
# print(f"Curso: {aluno.curso}")
# print("Disciplinas do aluno:")
# for disciplina in aluno.disciplinas:
#     print(disciplina)


# ======================== Questão 6 ========================
# Laptop herdando de Computer.
# ============================================================

# class Computer:
#     def __init__(self, model: str, speed: int) -> None:
#         self.model = model
#         self.speed = speed
#
#
# class Laptop(Computer):
#     def __init__(
#         self, model: str, speed: int, weight: int
#     ) -> None:
#         super().__init__(model, speed)
#         self.__weight = weight
#
#     @property
#     def weight(self) -> int:
#         return self.__weight
#
#     def __str__(self) -> str:
#         return (
#             f"{self.model}, {self.speed} MHz, "
#             f"{self.weight} kg"
#         )
#
#
# laptop = Laptop("Notebook Pro", 1500, 2)
# print(laptop)


# ======================== Questão 7 ========================
# Rectangle e Square.
# ============================================================

# class Rectangle:
#     def __init__(self, width: float, height: float) -> None:
#         self.width = width
#         self.height = height
#
#     def area(self) -> float:
#         return self.width * self.height
#
#     def __str__(self) -> str:
#         return (
#             f"Retângulo: {self.width} x {self.height}, "
#             f"área: {self.area()}"
#         )
#
#
# class Square(Rectangle):
#     def __init__(self, side: float) -> None:
#         super().__init__(side, side)
#
#     def __str__(self) -> str:
#         return (
#             f"Quadrado: lado {self.width}, "
#             f"área: {self.area()}"
#         )
#
#
# rectangle = Rectangle(5, 3)
# square = Square(4)
#
# print(rectangle)
# print(square)


# ======================== Questão 8 ========================
# Pagamentos com herança e polimorfismo.
# ============================================================

# class Pagamento:
#     def processar(self) -> None:
#         raise NotImplementedError(
#             "Método deve ser implementado"
#         )
#
#
# class PagamentoPix(Pagamento):
#     def processar(self) -> None:
#         print("Pagamento realizado via Pix!")
#
#
# class PagamentoCartao(Pagamento):
#     def processar(self) -> None:
#         print("Pagamento realizado via cartão!")
#
#
# pagamentos = [
#     PagamentoPix(),
#     PagamentoCartao(),
#     PagamentoPix(),
#     PagamentoCartao()
# ]
#
# for pagamento in pagamentos:
#     pagamento.processar()


# ======================== Questão 9 ========================
# Cartões comemorativos.
# ============================================================

# class CartaoMensagem:
#     def __init__(
#         self, destinatario: str, remetente: str
#     ) -> None:
#         self.destinatario = destinatario
#         self.remetente = remetente
#
#     def retornar_mensagem(self) -> str:
#         raise NotImplementedError(
#             "Método deve ser implementado"
#         )
#
#
# class CartaoNamorados(CartaoMensagem):
#     def retornar_mensagem(self) -> str:
#         return (
#             f"Feliz Dia dos Namorados, {self.destinatario}! "
#             f"Com amor, {self.remetente}."
#         )
#
#
# class CartaoNatal(CartaoMensagem):
#     def retornar_mensagem(self) -> str:
#         return (
#             f"Feliz Natal, {self.destinatario}! "
#             f"Boas festas! De: {self.remetente}."
#         )
#
#
# class CartaoAniversario(CartaoMensagem):
#     def retornar_mensagem(self) -> str:
#         return (
#             f"Feliz aniversário, {self.destinatario}! "
#             f"Muitas felicidades! De: {self.remetente}."
#         )
#
#
# destinatario = input("Nome do destinatário: ")
# remetente = input("Nome do remetente: ")
#
# cartoes = [
#     CartaoNamorados(destinatario, remetente),
#     CartaoNatal(destinatario, remetente),
#     CartaoAniversario(destinatario, remetente)
# ]
#
# for cartao in cartoes:
#     print()
#     print(cartao.retornar_mensagem())


# ======================== Questão 10 ========================
# Pedra, papel e tesoura.
# ============================================================

# import random
#
#
# class Jogador:
#     def __init__(self, nome: str) -> None:
#         self.nome = nome
#         self.escolha = None
#
#     def EscolherJogada(self) -> None:
#         raise NotImplementedError(
#             "Método deve ser implementado"
#         )
#
#
# class Humano(Jogador):
#     def EscolherJogada(self) -> None:
#         opcoes = ["pedra", "papel", "tesoura"]
#
#         while True:
#             escolha = input(
#                 "Escolha pedra, papel ou tesoura: "
#             ).strip().lower()
#
#             if escolha in opcoes:
#                 self.escolha = escolha
#                 break
#
#             print("Opção inválida! Tente novamente.")
#
#
# class Computador(Jogador):
#     def EscolherJogada(self) -> None:
#         self.escolha = random.choice(
#             ["pedra", "papel", "tesoura"]
#         )
#
#
# class Jogo:
#     def __init__(self) -> None:
#         self.jogador1 = Humano("Jogador")
#         self.jogador2 = Computador("Computador")
#
#         self.placar = {
#             "Jogador": 0,
#             "Computador": 0,
#             "Empates": 0
#         }
#
#     def DefineVencedor(self) -> None:
#         escolha1 = self.jogador1.escolha
#         escolha2 = self.jogador2.escolha
#
#         print(f"\nJogador escolheu: {escolha1}")
#         print(f"Computador escolheu: {escolha2}")
#
#         if escolha1 == escolha2:
#             print("Empate!")
#             self.placar["Empates"] += 1
#
#         elif (
#             (escolha1 == "pedra" and escolha2 == "tesoura")
#             or (escolha1 == "papel" and escolha2 == "pedra")
#             or (escolha1 == "tesoura" and escolha2 == "papel")
#         ):
#             print("Você venceu a rodada!")
#             self.placar["Jogador"] += 1
#
#         else:
#             print("O computador venceu a rodada!")
#             self.placar["Computador"] += 1
#
#     def JogarPartida(self) -> None:
#         while True:
#             self.jogador1.EscolherJogada()
#             self.jogador2.EscolherJogada()
#
#             self.DefineVencedor()
#
#             continuar = input(
#                 "\nDeseja jogar novamente? (s/n): "
#             ).strip().lower()
#
#             if continuar != "s":
#                 break
#
#         print("\n--- PLACAR FINAL ---")
#         for nome, pontos in self.placar.items():
#             print(f"{nome}: {pontos}")
#
#
# jogo = Jogo()
# jogo.JogarPartida()
