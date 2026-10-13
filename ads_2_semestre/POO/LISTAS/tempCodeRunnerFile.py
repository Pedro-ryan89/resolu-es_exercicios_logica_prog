class Contato:
    def __init__(self,nome: str,tell: str):
        self.__nome = nome
        self.__tell = tell
        
    @property
    def obter_contato(self) -> str:
        return self.__nome
    
    
    def __str__(self) -> str:
        return f"{self.__nome} - {self.__tell}"

    
    
class Agenda:
    def __init__(self):
        self.contatos = []
        
    def adicionar_contato(self, contato: Contato) -> None:
        self.contatos.append(contato)
        self.contatos.sort(key=lambda contato: contato.obter_contato)
        
        
    def remover_contato(self,contato: Contato) -> None:
        self.contatos.remove(contato)
            
    def exibir_contatos(self) -> None:
        for indice,contato in enumerate(self.contatos,start=1):
            print(f"{indice}. {contato}")
            
            
pedro = Contato("Pedro","12345678")
chico = Contato("chico dede","12345678")
sapao = Contato("sapao","12345678")

agenda = Agenda()

agenda.adicionar_contato(pedro)
agenda.adicionar_contato(chico)
agenda.adicionar_contato(sapao)

agenda.exibir_contatos()

print("\nREMOVENDO CONTATO\n")
agenda.remover_contato(sapao)

agenda.exibir_contatos()