def fibonacci(n):
    if (n == 1):
        return(0)
    elif (n == 2):
        return(1)
    else:
        f1 = 0
        f2 = 1
        for i in range(3, n+1):
            f3 = f1 + f2
            
            f1 = f2 # atualizando f1 e f2 para o próximo passo
            f2 = f3
            
        return(f3)
    
def fibonacci_recursivo(n):
    if (n == 1):
        return(0)
    elif (n == 2):
        return(1)
    else: # recursividade dupla (vira uma árvore)
        return(fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2))
            
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

# módulo principal (main)
for n in range(1, 16):
    print(fibonacci(n), end=" ")
print()
for n in range(1, 16):
    print(fibonacci_recursivo(n), end=" ")