#1° QUESTÃO: Classe Livro: Crie e teste uma classe que modele um livro:
class Livro:
    def __init__(self, titulo: str, autor: str, total_paginas: int, pagina_atual: int):
        self.titulo = titulo
        self.autor = autor
        self.total_paginas = total_paginas
        self.pagina_atual = pagina_atual
    def __str__(self):
        return f"O livro {self.titulo}, do(a) escritor(a) {self.autor} tem {self.total_paginas} páginas , atualmente está na página {self.pagina_atual} \n"
    def avancar_pagina (self):
        if(self.pagina_atual == self.total_paginas):
            print("Você já está na última página. \n")
        else:
            self.pagina_atual +=1
    def voltar_pagina (self):
        if(self.pagina_atual == 1):
            print("Você está na primeira página, não tem como voltar páginas. \n")
        else:
            self.pagina_atual -=1
    def ir_para_pagina(self, escolha):
        if(1<=escolha<=self.total_paginas):
            self.pagina_atual = escolha
        else:
            print("Número da página inválida.")

if (__name__ == "__main__"):
    dracula = Livro("Drácula","Bram Stoker", 650, 1)
    print(dracula)
    dracula.avancar_pagina()
    print(dracula)
    dracula.voltar_pagina()
    print(dracula)
    dracula.ir_para_pagina(-1)
    dracula.ir_para_pagina(50)
    print(dracula)
