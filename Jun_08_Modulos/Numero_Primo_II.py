from math import sqrt

def ehPrimo(n):
    if ((n == 0) or (n == 1)):
        return(False)
    else:
        fim = int(sqrt(n))
        for i in range(2, fim+1):
            if ((n % i) == 0):
                return(False)
        
        return(True)
        

# módulo principal
for n in range(20):
    if (ehPrimo(n)):
        print(f"{n}", end=" ")