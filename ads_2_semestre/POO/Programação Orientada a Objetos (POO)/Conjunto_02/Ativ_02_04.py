from datetime import datetime

agora = datetime.now()
print(agora)

natal = datetime(2026, 12, 25)
print(natal)
print(natal.day, natal.month, natal.year)
print(natal - agora)