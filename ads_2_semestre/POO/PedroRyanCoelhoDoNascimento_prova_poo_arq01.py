class Drone:
    def __init__(self,posicao_x:int = 0,posicao_y:int = 0,altura:int = 0):
        self.__posicao_x = posicao_x
        self.__posicao_y = posicao_y
        self.__altura = altura
        
    
    @property
    def altura(self):
        return self.__altura
        
    
    def voar(self,deslocamento_z: float):
        if  not isinstance(deslocamento_z,(int,float)):
            raise TypeError("O deslocamento vertical deve ser um número!")
        
        nova_altura = self.__altura + deslocamento_z
        if nova_altura >= 0 and nova_altura <= 120:
            self.__altura = nova_altura
        else:
            raise ValueError("A nova altura deve estar entre 0 e 120 metros!")
            
    @property
    def posicao_x(self):
        return self.__posicao_x
    
    @property
    def posicao_y(self):
        return self.__posicao_y
    
    def mover(self,deslocamento_x:float,deslocamento_y:float):
        if not isinstance(deslocamento_x,(int,float))  or not isinstance(deslocamento_y,(int,float)):
            raise TypeError("O deslocamento horizontal deve ser um número!")
            
        if self.__altura > 0:
            novo_x = self.__posicao_x + deslocamento_x
            novo_y = self.__posicao_y + deslocamento_y
            self.__posicao_x = novo_x
            self.__posicao_y = novo_y
        else:
            raise RuntimeError("Impossível mover, pois o drone está no chão!")
              
    def __str__(self):
        return f"Drone em {self.posicao_x,self.posicao_y} - Altura: {self.altura} m"
    

