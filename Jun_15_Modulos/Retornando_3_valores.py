def ordem(a, b, c):
    x = [a, b, c]
    
    x.sort()
    
    return(x[0], x[1], x[2])

# módulo principal (main)
a, b, c = ordem(1, 2, 3)
print(a, b, c)

a, b, c = ordem(3, 2, 1)
print(a, b, c)

a, b, c = ordem(2, 1, 3)
print(a, b, c)

a, b, c = ordem(2, 3, 1)
print(a, b, c)

a, b, c = ordem(1, 3, 2)
print(a, b, c)

a, b, c = ordem(3, 1, 2)
print(a, b, c)
