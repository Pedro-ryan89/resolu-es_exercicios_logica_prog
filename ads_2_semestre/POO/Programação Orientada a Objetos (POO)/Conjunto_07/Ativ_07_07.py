#7º QUESTÃO: Crie uma classe chamada WeatherStation, que será utilizada para armazenar observações
#sobre o clima. A classe deve possuir os seguintes métodos públicos:

class WeatherStation:
    def __init__(self, nome_estacao):
        self.__nome_estacao = nome_estacao
        self.__lista = []
    def add_observation (self, observation: str):
        self.__lista.append(observation)
    def latest_observation(self):
        if (len(self.__lista) == 0):
            return " "
        else:
            return f"{self.__lista[-1]}"
    def number_of_observations (self):
        return len(self.__lista)
    def __str__(self):
        return f"{self.__nome_estacao}, {len(self.__lista)} observations."

if (__name__ == "__main__"):
    station = WeatherStation ("K-DST")
    station.add_observation ("Rain 10mm")
    station.add_observation ("Sunny")
    print(station.latest_observation())
    station.add_observation("Thunderstorm")
    print(station.latest_observation())
    print(station.number_of_observations())
    print(station)