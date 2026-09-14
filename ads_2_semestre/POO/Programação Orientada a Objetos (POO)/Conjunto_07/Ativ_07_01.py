#1º QUESTÃO: Escreva uma classe para representar uma lâmpada. Desenvolva métodos para ligar, desligar,
#e imprimir o status da lâmpada. Não permita, usando encapsulamento, que o status da
#lâmpada seja alterado fora dos métodos ligar e desligar.
class Lampada:
    def __init__(self):
        self.__status = "desligada"
    def ligar (self):
        if(self.__status == "ligada"):
            print(f"A lâmpada já está {self.__status}.")
        else:
            self.__status = "ligada"
    def desligar (self):
        if(self.__status == "desligada"):
            print(f"A lâmpada já está {self.__status}.")
        else:
            self.__status = "desligada"
    def mostrar_status(self):
        return f"A lâmpada está {self.__status}."

if (__name__ == "__main__"):
    lampada_led = Lampada()
    lampada_led.status = "ligada"
    print(lampada_led.mostrar_status())
    lampada_led.__status = "ligada"
    print(lampada_led.mostrar_status())
    lampada_led.desligar()
    print(lampada_led.mostrar_status())
    lampada_led.ligar()
    print(lampada_led.mostrar_status())
    lampada_led.ligar()
    print(lampada_led.mostrar_status())


