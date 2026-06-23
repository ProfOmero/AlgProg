def ehPrimo(n):
    if ((n == 0) or (n == 1)):
        return(False)
    else:
        ctDiv = 0
        for i in range(1, n+1):
            if ((n % i) == 0):
                ctDiv = ctDiv + 1
        
        if (ctDiv == 2):
            return(True)
        else:
            return(False)
        

# módulo principal
for n in range(20):
    if (ehPrimo(n)):
        print(f"{n}", end=" ")