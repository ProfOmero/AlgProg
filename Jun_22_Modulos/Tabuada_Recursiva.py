def tabuada(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")
        
def tabuada_recursiva(i, n):
    if (i < 11):
        print(f"{n} x {i} = {n*i}")
        
        i = i + 1
        tabuada_recursiva(i, n) # recursividade = recorrer a si próprio


# módulo principal (main)
tabuada(7)
print()
tabuada_recursiva(1, 7)