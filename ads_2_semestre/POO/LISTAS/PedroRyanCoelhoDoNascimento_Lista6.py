
# ============================================================
# Lista de Exercícios 06 – Herança Múltipla, Classes Abstratas,
# Encapsulamento e Sobrecarga de Operadores.
# IFCE - Tecnologia em Análise e Desenvolvimento de Sistemas
# ============================================================


# ======================== Questão 1 ========================
# RPG com classes abstratas, herança e polimorfismo.
# ============================================================

# from abc import ABC, abstractmethod
# from random import randint
#
#
# class Personagem(ABC):
#     def __init__(self, nome: str, forca: int, vida: int = 100) -> None:
#         self.__nome = nome
#         self.__forca = forca
#         self.__vida = vida
#
#     @property
#     def nome(self) -> str:
#         return self.__nome
#
#     @property
#     def forca(self) -> int:
#         return self.__forca
#
#     @property
#     def vida(self) -> int:
#         return self.__vida
#
#     @vida.setter
#     def vida(self, valor: int) -> None:
#         self.__vida = max(0, min(100, valor))
#
#     @abstractmethod
#     def atacar(self) -> int:
#         pass
#
#     def sofrer_dano(self, dano: int) -> None:
#         self.vida = self.__vida - dano
#
#     def __str__(self) -> str:
#         return (
#             f"Classe: {self.__class__.__name__}\n"
#             f"Nome: {self.__nome}\n"
#             f"Força: {self.__forca}\n"
#             f"Vida: {self.__vida}"
#         )
#
#
# class Guerreiro(Personagem):
#     def __init__(self, nome: str) -> None:
#         super().__init__(nome, 70, 100)
#
#     def atacar(self) -> int:
#         dano = randint(1, self.forca)
#         print(f"{self.nome} usou Espada Reluzente!")
#         return dano
#
#
# class Mago(Personagem):
#     def __init__(self, nome: str) -> None:
#         super().__init__(nome, 60, 100)
#
#     def atacar(self) -> int:
#         dano = randint(1, self.forca)
#         print(f"{self.nome} usou Expecto Patronum!")
#         return dano
#
#
# class Arqueiro(Personagem):
#     def __init__(self, nome: str) -> None:
#         super().__init__(nome, 65, 100)
#
#     def atacar(self) -> int:
#         dano = randint(1, self.forca)
#         print(f"{self.nome} usou Disparo Sombrio!")
#         return dano
#
#
# # Herança múltipla: herda de Guerreiro e Mago.
# class Paladino(Guerreiro, Mago):
#     def __init__(self, nome: str) -> None:
#         Personagem.__init__(self, nome, 65, 100)
#
#     def atacar(self) -> int:
#         dano = randint(1, self.forca)
#         print(f"{self.nome} usou Golpe Sagrado!")
#         return dano
#
#
# class Arena:
#     def __init__(
#         self, personagem1: Personagem, personagem2: Personagem
#     ) -> None:
#         self.personagem1 = personagem1
#         self.personagem2 = personagem2
#
#     def duelo(self) -> None:
#         print("\n=== INÍCIO DO DUELO ===")
#         rodada = 1
#
#         while (
#             self.personagem1.vida > 0
#             and self.personagem2.vida > 0
#         ):
#             print(f"\n--- Rodada {rodada} ---")
#
#             dano = self.personagem1.atacar()
#             dano_real = min(dano, self.personagem2.vida)
#             self.personagem2.sofrer_dano(dano)
#
#             print(
#                 f"Dano causado: {dano_real} | "
#                 f"Vida de {self.personagem2.nome}: "
#                 f"{self.personagem2.vida}"
#             )
#
#             # O segundo personagem só ataca se estiver vivo.
#             if self.personagem2.vida > 0:
#                 dano = self.personagem2.atacar()
#                 dano_real = min(dano, self.personagem1.vida)
#                 self.personagem1.sofrer_dano(dano)
#
#                 print(
#                     f"Dano causado: {dano_real} | "
#                     f"Vida de {self.personagem1.nome}: "
#                     f"{self.personagem1.vida}"
#                 )
#
#             rodada += 1
#
#         if self.personagem1.vida > 0:
#             vencedor = self.personagem1
#         else:
#             vencedor = self.personagem2
#
#         print("\n=== FIM DO DUELO ===")
#         print(
#             f"Vencedor: {vencedor.nome} "
#             f"({vencedor.__class__.__name__})"
#         )
#
#
# # Testes dos personagens e das arenas.
# guerreiro = Guerreiro("Aragorn")
# mago = Mago("Gandalf")
# arqueiro = Arqueiro("Legolas")
# paladino = Paladino("Uther")
#
# arena1 = Arena(guerreiro, mago)
# arena1.duelo()
#
# arena2 = Arena(arqueiro, paladino)
# arena2.duelo()


# ======================== Questão 2 ========================
# SimpleDate: comparações entre datas.
# ============================================================

# class SimpleDate:
#     def __init__(self, dia: int, mes: int, ano: int) -> None:
#         if not 1 <= dia <= 30:
#             raise ValueError("O dia deve estar entre 1 e 30.")
#
#         if not 1 <= mes <= 12:
#             raise ValueError("O mês deve estar entre 1 e 12.")
#
#         self.__dia = dia
#         self.__mes = mes
#         self.__ano = ano
#
#     def __str__(self) -> str:
#         return f"{self.__dia}.{self.__mes}.{self.__ano}"
#
#     def __converter_para_dias(self) -> int:
#         return (
#             self.__ano * 360
#             + (self.__mes - 1) * 30
#             + self.__dia - 1
#         )
#
#     def __eq__(self, outro: object) -> bool:
#         if not isinstance(outro, SimpleDate):
#             return NotImplemented
#         return self.__converter_para_dias() == outro.__converter_para_dias()
#
#     def __ne__(self, outro: object) -> bool:
#         if not isinstance(outro, SimpleDate):
#             return NotImplemented
#         return self.__converter_para_dias() != outro.__converter_para_dias()
#
#     def __lt__(self, outro: object) -> bool:
#         if not isinstance(outro, SimpleDate):
#             return NotImplemented
#         return self.__converter_para_dias() < outro.__converter_para_dias()
#
#     def __gt__(self, outro: object) -> bool:
#         if not isinstance(outro, SimpleDate):
#             return NotImplemented
#         return self.__converter_para_dias() > outro.__converter_para_dias()
#
#
# d1 = SimpleDate(4, 10, 2020)
# d2 = SimpleDate(28, 12, 1985)
# d3 = SimpleDate(28, 12, 1985)
#
# print(d1)
# print(d2)
# print(d1 == d2)
# print(d1 != d2)
# print(d1 == d3)
# print(d1 < d2)
# print(d1 > d2)


# ======================== Questão 3 ========================
# SimpleDate: incremento e diferença entre datas.
# ============================================================

# class SimpleDate:
#     def __init__(self, dia: int, mes: int, ano: int) -> None:
#         if not 1 <= dia <= 30:
#             raise ValueError("O dia deve estar entre 1 e 30.")
#
#         if not 1 <= mes <= 12:
#             raise ValueError("O mês deve estar entre 1 e 12.")
#
#         self.__dia = dia
#         self.__mes = mes
#         self.__ano = ano
#
#     def __str__(self) -> str:
#         return f"{self.__dia}.{self.__mes}.{self.__ano}"
#
#     def __converter_para_dias(self) -> int:
#         return (
#             self.__ano * 360
#             + (self.__mes - 1) * 30
#             + self.__dia - 1
#         )
#
#     @staticmethod
#     def __converter_de_dias(total_dias: int):
#         ano, resto = divmod(total_dias, 360)
#         mes, resto = divmod(resto, 30)
#         dia = resto + 1
#         return SimpleDate(dia, mes + 1, ano)
#
#     def __add__(self, dias: int):
#         if not isinstance(dias, int):
#             return NotImplemented
#
#         total = self.__converter_para_dias() + dias
#         return SimpleDate.__converter_de_dias(total)
#
#     def __sub__(self, outra):
#         if not isinstance(outra, SimpleDate):
#             return NotImplemented
#
#         diferenca = (
#             self.__converter_para_dias()
#             - outra.__converter_para_dias()
#         )
#         return abs(diferenca)
#
#
# # Testes de incremento.
# d1 = SimpleDate(4, 10, 2020)
# d2 = SimpleDate(28, 12, 1985)
#
# d3 = d1 + 3
# d4 = d2 + 400
#
# print(d1)
# print(d2)
# print(d3)
# print(d4)
#
# # Testes de diferença.
# d5 = SimpleDate(2, 11, 2020)
#
# print(d5 - d1)
# print(d1 - d5)
# print(d1 - d2)


# ======================== Questão 4 ========================
# Desafio Final – Formas geométricas, herança múltipla e
# sobrecarga de operadores.
# ============================================================

# from abc import ABC, abstractmethod
# from math import pi
#
#
# class Forma(ABC):
#     @abstractmethod
#     def area(self) -> float:
#         pass
#
#     # Compara formas de acordo com suas áreas.
#     def __gt__(self, outra) -> bool:
#         if not isinstance(outra, Forma):
#             return NotImplemented
#         return self.area() > outra.area()
#
#     def __lt__(self, outra) -> bool:
#         if not isinstance(outra, Forma):
#             return NotImplemented
#         return self.area() < outra.area()
#
#     def __eq__(self, outra) -> bool:
#         if not isinstance(outra, Forma):
#             return NotImplemented
#         return self.area() == outra.area()
#
#
# class Retangulo(Forma):
#     def __init__(self, largura: float, altura: float) -> None:
#         self.largura = largura
#         self.altura = altura
#
#     def area(self) -> float:
#         return self.largura * self.altura
#
#     def __str__(self) -> str:
#         return (
#             f"Retângulo: {self.largura} x {self.altura}, "
#             f"área: {self.area()}"
#         )
#
#
# class Circulo(Forma):
#     def __init__(self, raio: float) -> None:
#         self.raio = raio
#
#     def area(self) -> float:
#         return pi * self.raio ** 2
#
#     def __str__(self) -> str:
#         return (
#             f"Círculo: raio {self.raio}, "
#             f"área: {self.area():.2f}"
#         )
#
#
# class Colorivel:
#     def __init__(self, cor: str) -> None:
#         # Atributo protegido.
#         self._cor = cor
#
#     @property
#     def cor(self) -> str:
#         return self._cor
#
#     def alterar_cor(self, nova_cor: str) -> None:
#         self._cor = nova_cor
#
#
# # Herança múltipla: retângulo com características de cor.
# class RetanguloColorido(Retangulo, Colorivel):
#     def __init__(
#         self, largura: float, altura: float, cor: str
#     ) -> None:
#         Retangulo.__init__(self, largura, altura)
#         Colorivel.__init__(self, cor)
#
#     def __str__(self) -> str:
#         return (
#             f"Retângulo colorido: {self.largura} x {self.altura}, "
#             f"cor: {self.cor}, área: {self.area()}"
#         )
#
#
# # Testes das formas.
# retangulo = Retangulo(5, 4)
# circulo = Circulo(3)
# retangulo_colorido = RetanguloColorido(6, 4, "Azul")
#
# print(retangulo)
# print(circulo)
# print(retangulo_colorido)
#
# print("\n--- Comparações ---")
# print(retangulo > circulo)
# print(retangulo < circulo)
# print(retangulo == retangulo_colorido)
#
# print("\n--- Alteração de cor ---")
# print(f"Cor original: {retangulo_colorido.cor}")
# retangulo_colorido.alterar_cor("Vermelho")
# print(f"Nova cor: {retangulo_colorido.cor}")
