#6º QUESTÃO:Classe Personagem: Criando um Sistema de Batalha

class Personagem:
    def __init__(self, nome: str, vida: int = 100, ataque: int = 10, nivel: int = 1):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.nivel = nivel
    def __str__(self):
        return f"Nome: {self.nome} | Nível: {self.nivel} | Vida: {self.vida} | Ataque: {self.ataque}"
    def receber_dano (self, vilão: "Personagem"):
        self.vida -= vilão.ataque
        if(self.vida > 0):
            print(f"{self.nome} agora tem {self.vida} de vida.")
        else:
            print(f"{self.nome} foi derrotado!")
    def atacar (self, inimigo: "Personagem"):
        print(f"{self.nome} atacou o {inimigo.nome} causando {self.ataque} de dano!")
        inimigo.receber_dano(self)
    def subir_nivel(self):
        self.nivel +=1
        self.ataque +=5
        self.vida +=20
        return f"{self.nome} evoluiu para o nível {self.nivel}!"

rockeiro = Personagem("Rockeiro", 120, 12)
pirangueiro = Personagem("Pirangueiro", 150, 15)
rockeiro.atacar(pirangueiro)
pirangueiro.atacar(rockeiro)
rockeiro.subir_nivel()
print(rockeiro)