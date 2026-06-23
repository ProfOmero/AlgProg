def repetir(tipo='.', n=20):
    result = ""
    for i in range(n):
        result = result + tipo
        
    return(result)

# módulo principal (main)
print(repetir('.', 20))
print(repetir())
print(repetir('*'))
print(repetir('X', 40))
print(repetir('ABC', 10))
