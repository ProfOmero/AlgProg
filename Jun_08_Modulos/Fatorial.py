def fatorial(n):
    if (n < 0):
        f = 0
    else:
        f = 1
        for i in range(1, n+1):
            f = f * i
        
    return(f)
        

# módulo principal
for n in range(0, 11):
    print(f"{n}! = {fatorial(n)}")