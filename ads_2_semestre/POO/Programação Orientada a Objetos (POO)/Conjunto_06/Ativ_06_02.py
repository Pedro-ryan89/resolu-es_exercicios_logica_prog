class Usuario:
    total_usuarios = 0

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        Usuario.total_usuarios +=1

    @classmethod
    def criar_por_texto(cls, texto):
        nome, idade = texto.split(",")
        return cls(nome, int(idade))

    def mostrar_total_usuario():
        return Usuario.total_usuarios

user = Usuario.criar_por_texto("Eduardo, 25")
user1 = Usuario.criar_por_texto ("Daniel, 18")
print (Usuario.mostrar_total_usuario())