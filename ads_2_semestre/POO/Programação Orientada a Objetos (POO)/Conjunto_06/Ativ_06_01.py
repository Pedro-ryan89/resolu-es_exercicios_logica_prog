class Produto:
    imposto = 0.1
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    def __str__(self):
        return f"{self.nome} - R${self.preco + self.preco * Produto.imposto}"
    def preco_final(self):
        return f"O valor original de {self.nome} é de R${self.preco}. Com o imposto de R${self.preco * self.imposto}, fica R${self.preco + self.preco * Produto.imposto}."

coisa = Produto("Arroz", 3.99)
print(coisa)
print(coisa.preco_final())