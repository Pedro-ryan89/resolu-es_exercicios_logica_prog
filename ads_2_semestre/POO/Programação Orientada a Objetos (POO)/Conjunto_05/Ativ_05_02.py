#2° QUESTÃO: Classe Cronômetro (Stopwatch): Considere a seguinte estrutura para a classe Stopwatch:
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
    def tick(self):
        if(self.seconds == 59):
            self.minutes +=1
            self.seconds = 0
        else:
            self.seconds +=1
        if(self.minutes > 59):
            self.minutes = 0
            self.hours +=1
if(__name__ == "__main__"):
    watch = Stopwatch()
    for i in range(3601):
        print(watch)
        watch.tick()