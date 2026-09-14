class Livro:
    def __init__(self, titulo, paginas):
        self.__titulo = titulo
        self.__paginas = paginas

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, novo_titulo):
        if(self.__titulo != novo_titulo):
            self.__titulo = novo_titulo
        else:
            raise Exception ("Mesmo título.")

    @property
    def pagina (self):
        return self.__paginas

    @pagina.setter
    def pagina (self, novo_numero_paginas):
        if(self.__paginas != novo_numero_paginas and novo_numero_paginas > 0):
            self.__paginas = novo_numero_paginas
        else:
            raise Exception ("Valores negativos não são permitidos.")

if (__name__ == "__main__"):
    harry_potter = Livro("Harry Potter e a Pedra Filosofal", 330)
    print(harry_potter.titulo)
    harry_potter.titulo = "Harry Potter e o Prisioneiro de Azkaban"
    print(harry_potter.titulo)