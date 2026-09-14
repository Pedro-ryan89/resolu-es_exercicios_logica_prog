#3° QUESTÃO: Defina uma nova classe chamada Clock que expanda as capacidades da sua classe Stopwatch. 
# Ela deve funcionar da seguinte forma:


class Clock:
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours
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
        if(self.hours == 24):
            self.hours = 0
    def set(self, new_hour = 0, new_minute = 0, new_second = 0):
        self.hours = new_hour
        self.minutes = new_minute
        self.seconds = new_second


if (__name__ == "__main__"):
    clock = Clock(23, 59, 55)
    for i in range(6):
        print(clock)
        clock.tick()
    clock.set(12,5)
    print(clock)
