def mostrar(i, n):
    if (i <= n):
        if (i == 1):
            print("{", end="")
        print(f"{i}", end="")
        if (i <= (n-1)):
            print(", ", end="")
            
        i = i + 1 # passo para a variável "i"
        mostrar(i, n) # recursividade
    else:
        print("}")
        
def somar(i, n):
    if (i <= n):
        vlr = i
        
        i = i + 1
        return(vlr + somar(i, n)) # recursividade
    else:
        return(0)
            

# módulo principal (main)
mostrar(1, 9)
print(f"soma = {somar(1, 9)}")
print()
mostrar(1, 7)
print(f"soma = {somar(1, 7)}")