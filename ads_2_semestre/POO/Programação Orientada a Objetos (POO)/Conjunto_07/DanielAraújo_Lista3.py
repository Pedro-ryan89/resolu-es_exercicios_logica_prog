#1º QUESTÃO: Escreva uma classe para representar uma lâmpada. Desenvolva métodos para ligar, desligar,
#e imprimir o status da lâmpada. Não permita, usando encapsulamento, que o status da
#lâmpada seja alterado fora dos métodos ligar e desligar.
class Lampada:
    def __init__(self):
        self.__status = "desligada"
    def ligar (self):
        if(self.__status == "ligada"):
            print(f"A lâmpada já está {self.__status}.")
        else:
            self.__status = "ligada"
    def desligar (self):
        if(self.__status == "desligada"):
            print(f"A lâmpada já está {self.__status}.")
        else:
            self.__status = "desligada"
    def mostrar_status(self):
        return f"A lâmpada está {self.__status}."

if (__name__ == "__main__"):
    lampada_led = Lampada()
    lampada_led.status = "ligada"
    print(lampada_led.mostrar_status())
    lampada_led.__status = "ligada"
    print(lampada_led.mostrar_status())
    lampada_led.desligar()
    print(lampada_led.mostrar_status())
    lampada_led.ligar()
    print(lampada_led.mostrar_status())
    lampada_led.ligar()
    print(lampada_led.mostrar_status())
print("")

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

#from Ativ_07_02_classe import Ponto
import random

alfabeto = ["A","B","C","D","E","F","G","H","I","J"]
pontos = []
for i in alfabeto:
    i = Ponto.criar(f"Ponto {i},{random.randint(-100, 100)},{random.randint(-100, 100)}")
    pontos.append(i)
for i in pontos:
    print(i)
print("")

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

#from Ativ_07_03_classe import Ponto

Ponto1 = Ponto.criar("Ponto1,1,2")
Ponto2 = Ponto.criar("Ponto2,3,4")
Ponto1.calcularDistancia(Ponto2)
Ponto2.calcularDistancia(Ponto1)
print("")

#4º QUESTÃO: Crie uma classe Funcionário para armazenar as informações de um Funcionário. A classe
#deve armazenar o nome, o cargo o valor da hora trabalhada, a quantidade de horas
#trabalhadas e o salário. Esses dois últimos parâmetros não devem ser públicos.

class Funcionario:
    def __init__(self, nome, cargo, valor_hora=100):
        self.nome = nome
        self.cargo = cargo
        self.valor_hora = valor_hora
        self.__salario = 0
        self.__quantidade_horas = 0

    def registrar_hora(self):
        self.__quantidade_horas +=1
        self.calcular_salario()

    def calcular_salario (self):
        self.__salario = self.__quantidade_horas * self.valor_hora

    @property
    def salario(self):
        return f"R${self.__salario:.2f}"

    @salario.setter
    def salario(self, valor):
        raise Exception ("Não é permitido alterar o valor do salário manualmente")

if (__name__ == "__main__"):
    daniel = Funcionario("Daniel", "Programador")
    daniel.calcular_salario()
    print(daniel.salario)
    daniel.registrar_hora()
    daniel.calcular_salario()
    print(daniel.salario)
print("")

#5º QUESTÃO: Crie uma classe Elevador para armazenar as informações de um elevador de prédio. A classe
#deve armazenar o andar atual (térreo = 0), total de andares no prédio (desconsiderando o
#térreo), a capacidade do elevador e quantas pessoas estão presentes nele.

class Elevador:
    def __init__(self, capacidade_elevador, total_andares):
        self.__capacidade_atual = 0
        self.__andar_atual = 0
        self.__capacidade_elevador = capacidade_elevador
        self.__total_andares = total_andares

    def entrar(self):
        if (self.__capacidade_atual < self.__capacidade_elevador):
            self.__capacidade_atual +=1
        else:
            print("O elevador está cheio. Aguarde e tente novamente.")

    def sair(self):
        if (self.__capacidade_atual > 0):
            self.__capacidade_atual -=1
        else:
            print("O elevador está vazio. Não há ninguém para sair.")

    def subir(self):
        if (self.__andar_atual < self.__total_andares):
            self.__andar_atual +=1deslocamento_z
        else:
            print("Uso inválido de método.")

    # def subir(self, andar):
    #     if (andar <= self.__total_andares and andar > self.__andar_atual):
    #         self.__andar_atual = andar
    #     else:
    #         print("Uso inválido de método.")

    # def descer(self, andar):
    #     if (andar >= 0 and andar < self.__andar_atual):
    #         self.__andar_atual = andar
    #     else:
    #         print("Uso inválido de método.")

    def descer(self):
        if(self.__andar_atual > 0):
            self.__andar_atual -=1
        else:
            print("Uso indevido de método.")

if (__name__ == "__main__"):
    elevador_faculdade = Elevador(10, 2)
    for i in range(11):
        elevador_faculdade.entrar()
    for i in range(11):
        elevador_faculdade.sair()
    # elevador_faculdade.subir(0) #Uso inválido de método. Já está nesse andar.
    # elevador_faculdade.subir(3) #Uso inválido de método. Excede o número de andares.
    # elevador_faculdade.subir(2)
    # elevador_faculdade.subir(1) #Uso inválido de método. Tentando descer com o método subir()
    # elevador_faculdade.descer(3) #Uso inválido de método. Excede o número de andares.
    # elevador_faculdade.descer(2) #Uso inválido de método. Já está nesse andar.
    # elevador_faculdade.descer(1)
    # elevador_faculdade.descer(2) #Uso inválido de método. Tentando subir com o método descer()
    for i in range(3):
        elevador_faculdade.subir()
    for i in range(3):
        elevador_faculdade.descer()

    #Optei por colocar parâmetros nos métodos subir() e descer() por ficar mais próximo do uso
    #real de um elevador. Para colocar os métodos da forma que a questão pede, é só selecionar
    #inverter os métodos e os testes dos métodos em comentários pelos que estão implementados no momento.
print("")

#6º QUESTÃO: Crie uma classe chamada Recording que represente uma única gravação. A classe deve
#possuir uma variável privada: __length, do tipo inteiro.
#Implemente os seguintes itens:

class Recording:
    def __init__(self, length: int):
        if(length < 0):
            raise ValueError ("Valor negativo não é permitido.")
        else:
            self.__length = length

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        if(length < 0):
            raise ValueError ("Valor negativo não é permitido.")
        else:
            self.__length = length

if (__name__ == "__main__"):
    the_wall = Recording(43)
    print(the_wall.length)
    the_wall.length = 44
    print(the_wall.length)
print("")

#7º QUESTÃO: Crie uma classe chamada WeatherStation, que será utilizada para armazenar observações
#sobre o clima. A classe deve possuir os seguintes métodos públicos:

class WeatherStation:
    def __init__(self, nome_estacao):
        self.__nome_estacao = nome_estacao
        self.__lista = []
    def add_observation (self, observation: str):
        self.__lista.append(observation)
    def latest_observation(self):
        if (len(self.__lista) == 0):
            return " "
        else:
            return f"{self.__lista[-1]}"
    def number_of_observations (self):
        return len(self.__lista)
    def __str__(self):
        return f"{self.__nome_estacao}, {len(self.__lista)} observations."

if (__name__ == "__main__"):
    station = WeatherStation ("K-DST")
    station.add_observation ("Rain 10mm")
    station.add_observation ("Sunny")
    print(station.latest_observation())
    station.add_observation("Thunderstorm")
    print(station.latest_observation())
    print(station.number_of_observations())
    print(station)