class Produto:
    imposto = 0.10

    def __init__(self, nome: str, preco: int) -> None:
        self.nome = nome
        self.preco = preco

    def preco_final(self):
        imp_final = self.preco * Produto.imposto
        return imp_final + self.preco


produto = Produto("teste", 50)
print(produto.preco_final())
