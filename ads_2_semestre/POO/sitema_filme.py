class Filme:
    
    generos = ["ação", "comédia", "drama", "ficção", "terror"]
    
    def __init__(self,titulo: str,diretor: str,ano: int,genero: str) -> None:
        self.__titulo = titulo.upper()
        self.__diretor = diretor.upper()
        self.__ano = ano
        self.__genero = genero.upper()
        
        if not self.genero.lower() in self.generos:
            raise ValueError("genero nao aceito no catalogo")
    
    @property
    def titulo(self):
        return self.__titulo


    @property
    def diretor(self):
        return self.__diretor
        
        
    @property
    def ano(self):
        return self.__ano
        
        
    @property
    def genero(self):
        return self.__genero
                  
            
            
    def __str__(self) -> str:
        return f"titulo: {self.__titulo} | diretor: {self.__diretor} | ano: {self.__ano} | genero: {self.__genero}"
  
  
      
class Catalogo:
    
    def __init__(self) -> None:
        self.filmes = []
    
    def adicionar_filme(self,filme: Filme):
        if not isinstance(filme, Filme):
            raise TypeError("O objeto precisa ser um Filme.")
        self.filmes.append(filme)
        
    def remover_filme(self,titulo: str):
        for filme in self.filmes:
            if filme.titulo == titulo.upper():
                self.filmes.remove(filme)
                return
            
        raise ValueError("Filme não encontrado.")
    
    def listar_filme(self,genero):
        if genero == "":
            for filme in self.filmes:
                print(filme)
            return
                
        encontrou = False
        
        for filme in self.filmes:
            if filme.genero == genero.upper():
                print(filme)
                encontrou = True
            
        if not encontrou:
            raise ValueError("filme nao encontrado")
                
        
        

if __name__=="__main__":
    
    c = Catalogo()

    
    f1 = Filme("300", "Zack Snyder", 2006, "drama")
    f2 = Filme("Matrix", "Wachowski", 1999, "ficção")
    f3 = Filme("O Iluminado", "Stanley Kubrick", 1980, "terror")

   
    c.adicionar_filme(f1)
    c.adicionar_filme(f2)
    c.adicionar_filme(f3)

    
    print("\n--- FILMES DE FICÇÃO ---")
    c.listar_filme("ficção")

    print("\n--- FILMES DE TERROR ---")
    c.listar_filme("terror")

    print("\n--- REMOVENDO MATRIX ---")
    c.remover_filme("Matrix")
    c.listar_filme("") # aqui se ele nao recebe nada ele so mostrar tudo mesmo