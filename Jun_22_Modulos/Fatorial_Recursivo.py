def fatorial(n):
    if (n < 0):
        return(0)
    else:
        f = 1
        for i in range(1, n+1):
            f = f * i
        return(f)
    
def fatorial_recursivo(n):
    if (n < 0):
        return(0)
    elif (n == 0):
        return(1) # vai desempilhar as chamadas recursivas
    else:
        return(n * fatorial_recursivo(n-1)) # recursividade
    
# módulo principal (main)
print(f"7! = {fatorial(7)}")
print()
print(f"7! = {fatorial_recursivo(7)}")
