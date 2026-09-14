#3º QUESTÃO: Aproveitando a classe Ponto da questão 3, adicione o método calcularDistancia(), que
#receba um outro ponto como argumento e calcule a distância euclidiana entre eles.
#Considerando dois pontos (P e Q), a distância euclidiana é calculada pela fórmula:

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

    def calcularDistancia(self, ponto2):
        print (f"A distância entre {self.__nome} e {ponto2.__nome} é de: {((self.__x - ponto2.__x)**2 + (self.__y - ponto2.__y)**2)**0.5}")
    @classmethod
    def criar(cls, texto):
        cls.__permitir_criacao = True
        nome, x, y = texto.split(",")
        return cls(nome, int(x), int(y))