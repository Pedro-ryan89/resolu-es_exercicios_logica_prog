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
            self.__andar_atual +=1
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

