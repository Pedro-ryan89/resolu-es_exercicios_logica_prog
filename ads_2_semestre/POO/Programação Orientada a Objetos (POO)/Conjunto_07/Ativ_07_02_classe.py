#2º QUESTÃO: Crie uma classe Ponto, conforme a figura a seguir. O método __str__ deve retornar os
#atributos do objeto no formato “nome: (x, y)”. Crie em outro arquivo os testes para a
#classe Ponto, lendo diversos pontos e criando um objeto ponto para cada entrada lida.
#Coloque cada objeto da classe Ponto em uma lista e, ao final, imprima cada elemento dessa
#lista.
class Ponto:
    __permitir_criacao = False
    def __init__(self, nome: str, x: int, y: int):
        if(Ponto.__permitir_criacao == False):
            raise Exception ("Objetos só devem ser criados por métodos da classe.")
        self.__nome = nome
        self.__x = x
        self.__y = y

        Ponto.__permitir_criacao = False

    def __str__(self):
        return f"{self.__nome}: ({self.__x}, {self.__y})"
    @classmethod
    def criar(cls, texto):
        cls.__permitir_criacao = True
        nome, x, y = texto.split(",")
        return cls(nome, int(x), int(y))