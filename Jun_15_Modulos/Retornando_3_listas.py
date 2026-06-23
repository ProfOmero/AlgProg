def separar(a):
    negativos = []
    neutros = []
    positivos = []
    
    for i in range(len(a)):
        if (a[i] < 0):
            negativos.append(a[i])
        elif (a[i] == 0):
            neutros.append(a[i])
        else:
            positivos.append(a[i])
    
    return(negativos, neutros, positivos)

# módulo principal (main)
x = [-1, 0, 5, -2, 1, 9, 4, -3, -9, -5, 0, 4, -1, -8, 6, -4, 4, 5]

a, b, c = separar(x)

print(x)
print(a)
print(b)
print(c)
    
