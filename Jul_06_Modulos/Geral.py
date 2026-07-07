from os import system
from time import sleep

def parada():
    print("Pressione [ENTER] para prosseguir. ", end="")
    input()
    
def delay(tempo): # "tempo" em segundos
    sleep(tempo)