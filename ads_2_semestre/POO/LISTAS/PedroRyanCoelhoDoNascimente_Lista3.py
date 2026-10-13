# ============================================================
# Lista de Exercícios 03 - ENCAPSULAMENTO
# IFCE - Tecnologia em Analise e Desenvolvimento de Sistemas
# ============================================================


# ======================== Questão 1 ========================

# class Lampada:
#     def __init__(self) -> None:
#         self.__ligada = False
        
#     def ligar(self):
#         self.__ligada = True
    
#     def desligar(self):
#         self.__ligada = False
    
    
#     def estado(self):
#         if self.__ligada:
#             return f"a lampada esta  ligada"
#         else:
#             return f"a lampada esta  desligada"
        
# luz = Lampada()

# luz.ligar() 
# print(luz.estado())

# luz.desligar()
# print(luz.estado())

# ======================== Questão 2-3========================

# class Ponto:
#     def __init__(self,nome: str,x: int = 0,y:int = 0) -> None:
#         self.nome = nome
#         self.x = x
#         self.y = y
        
    
#     def __str__(self) -> str:
#         return f"{self.nome}: {self.x} , {self.y}"

#     def calcularDistancia(self,p):
#         d = ((self.x - p.x)**2 + (self.y - p.y)**2)**0.5
#         return d 
        
    
# pontos = []
# ponto1 = Ponto("ponto 1",45,87)
# ponto2 = Ponto("Ponto 2", 30, 40)
# pontos.append(ponto1)
# pontos.append(ponto2)

# for ponto in pontos:
#     print(ponto) 
    
# print(f"\nDistância entre {ponto1.nome} e {ponto2.nome}:")
# print(f"{ponto1.calcularDistancia(ponto2):.2f}")


# ======================== Questão 4 ========================

# class Funcionario:
#     def __init__(self,nome: str,cargo: str,valor_hora_trabalhada:float = 100):
#         self.nome = nome
#         self.cargo = cargo
#         self.valor_hora_trabalhada = valor_hora_trabalhada
#         self.__qt_horas = 0
#         self.__salario = 0
        
#     @property
#     def mostrar_horas(self) -> float:
#         return self.__qt_horas
        
#     @property
#     def salario(self):
#         return self.__salario
    
#     @salario.setter
#     def salario(self,valor):
#         raise AttributeError("o salario nao pode ser alterado diretamente")
    
#     def calcular_salario(self):
#         self.__salario = self.__qt_horas * self.valor_hora_trabalhada
#         return self.__salario
        
        
#     def registra_hora(self,horas_de_trabaho: float) -> None:
#         if horas_de_trabaho > 0:
#             self.__qt_horas += horas_de_trabaho
            
    
# f = Funcionario("Pedro", "Programador", 100)
# f.registra_hora(8)

# f.salario = 5000 # raise error
# print(f.calcular_salario())
# print(f.salario)


# ======================== Questão 5 ========================

# class Elevador:
#     def __init__(self,capacidade_elevador: int,total_andares: int) -> None:
#         self.__andar_atual = 0
#         self.__total_andares = total_andares
#         self.__capacidade_elevador = capacidade_elevador
#         self.__qt_pessoas = 0
        
        
#     def entrar(self,p_entrando: int) -> None:
#         espaco_disponivel = self.__capacidade_elevador - self.__qt_pessoas
#         total = self.__qt_pessoas + p_entrando
        
#         if p_entrando <= espaco_disponivel:
#             self.__qt_pessoas += p_entrando
#         else:
#             self.__qt_pessoas = self.__capacidade_elevador
#             pessoas_fora = p_entrando - espaco_disponivel
            
#             print(
#                 f"Elevador cheio"
#                 f"total de pessoas fora: {pessoas_fora}"
                
#             )
           
#     def sair(self) -> None:
#         if self.__qt_pessoas > 0:
#             self.__qt_pessoas -= 1
#         else:
#             print("nao há ninguem no elevador")
            
#     def subir_andar(self) -> None:
#         if self.__andar_atual < self.__total_andares:
#             self.__andar_atual += 1
        
#     def descer(self):
#         if self.__andar_atual > 0:
#             self.__andar_atual -= 1
            
#     def __str__(self) -> str:
#      return f"ELEVADOR:\nquantidade de pessoas: {self.__qt_pessoas} | andar atual: {self.__andar_atual} | capacidade: {self.__capacidade_elevador}"

# elevador = Elevador(5, 5)

# elevador = Elevador(5, 5)

# print("=== ELEVADOR INICIAL ===")
# print(elevador)


# print("\n=== ENTRANDO 3 PESSOAS ===")
# elevador.entrar(3)
# print(elevador)


# print("\n=== TENTANDO ENTRAR MAIS 3 PESSOAS ===")
# elevador.entrar(3)
# print(elevador)


# print("\n=== ENTRANDO MAIS 1 PESSOA ===")
# elevador.entrar(1)
# print(elevador)


# print("\n=== SAINDO 1 PESSOA ===")
# elevador.sair()
# print(elevador)


# print("\n=== SUBINDO 1 ANDAR ===")
# elevador.subir_andar()
# print(elevador)


# print("\n=== SUBINDO ATÉ O ÚLTIMO ANDAR ===")
# elevador.subir_andar()
# elevador.subir_andar()
# elevador.subir_andar()
# elevador.subir_andar()
# print(elevador)


# print("\n=== TENTANDO SUBIR ALÉM DO ÚLTIMO ANDAR ===")
# elevador.subir_andar()
# print(elevador)


# print("\n=== DESCENDO 1 ANDAR ===")
# elevador.descer()
# print(elevador)


# print("\n=== DESCENDO ATÉ O TÉRREO ===")
# elevador.descer()
# elevador.descer()
# elevador.descer()
# elevador.descer()
# print(elevador)


# print("\n=== TENTANDO DESCER ABAIXO DO TÉRREO ===")
# elevador.descer()
# print(elevador)


# print("\n=== RETIRANDO TODAS AS PESSOAS ===")
# elevador.sair()
# elevador.sair()
# elevador.sair()
# elevador.sair()
# print(elevador)


# print("\n=== TENTANDO RETIRAR PESSOA COM ELEVADOR VAZIO ===")
# elevador.sair()
# print(elevador)


# ======================== Questão 6 ========================


# class Recording:
#     def __init__(self,length: int) -> None:
#         self.__length = length
#         if self.__length == 0:
#             raise ValueError("valor menor que zero")
        
#     @property
#     def length(self):
#         return self.__length
    
#     @length.setter
#     def length(self,new_recording) -> None:
#         if new_recording == 0:
#             raise ValueError("valor menor que zero")
#         else:
#             self.__length = new_recording
    

# the_wall = Recording(43) 
# print(the_wall.length) 
# the_wall.length = 44 
# print(the_wall.length)
        
        
# ======================== Questão 7 ========================

class WeatherStation:
    def __init__(self,nome_estacao: str) -> None:
        self.__nome_estacao = nome_estacao
        self.__observations = []
        
        
    def add_observation(self,observation: str) -> None:
        self.__observations.append(observation)
    
    def latest_observation(self) ->str:
        if len(self.__observations) == 0:
            return ""
        
        return self.__observations[-1]
        
    def number_of_observations(self) -> int:
        return len(self.__observations)
        
        
    def __str__(self) -> str:
        return f"{self.__nome_estacao}, {self.number_of_observations()} observations"
        




station = WeatherStation("Houston")
station.add_observation("Rain 10mm")
station.add_observation("Sunny")
print(station.latest_observation())

station.add_observation("Thunderstorm")
print(station.latest_observation())

print(station.number_of_observations())
print(station)