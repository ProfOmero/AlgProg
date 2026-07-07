from Geral import delay, parada
from random import randint

for i in range(10):
    nro = randint(1, 100)    
    print(f"{i+1}o. número = {nro}")
    delay(1)
    
print()
parada()