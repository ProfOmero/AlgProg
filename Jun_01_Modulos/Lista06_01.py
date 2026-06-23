def maior(a, b):
    if (a >= b):
        return(a)
    else:
        return(b)
    
# módulo principal (main)
a = int(input())
b = int(input())

print(f"{a}, {b} {{{maior(a, b)} é o maior}}")