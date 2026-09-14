class Usuario:
    total_usuarios = 0  # atributo da classe

    def __init__(self, nome, idade):
        self.nome = nome  # Dado do objeto
        self.idade = idade  # Dado do objeto
        Usuario.total_usuarios += 1

    @classmethod
    def criar_por_texto(cls, texto):
        nome, idade = texto.split(",")
        return cls(nome, int(idade))

    @classmethod
    def mostrar_total_de_usuarios(cls):
        print(f"total de usuarios {cls.total_usuarios}")


# criando o primeiro objeto
user1 = Usuario("pedro", 21)

# craindo o segundo objeto usando um metodo pertecente a propria classe
user2 = Usuario.criar_por_texto("pedro,21")

# chamada pela propria classe ja que e um metodo da propria classe
Usuario.mostrar_total_de_usuarios()
