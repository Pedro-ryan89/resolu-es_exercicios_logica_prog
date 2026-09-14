#4º QUESTÃO: Escreva uma classe chamada Pessoa com um único atributo chamado nome, que deve ser 
# definido por meio de um argumento passado ao construtor.

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def retorna_primeiro_nome(self):
        return self.nome.split(" ")[0]
    
    def retorna_ultimo_nome(self):
        return self.nome.split(" ")[1]
    
daniel = Pessoa("Daniel Araújo")

print(daniel.retorna_primeiro_nome())
print(daniel.retorna_ultimo_nome())