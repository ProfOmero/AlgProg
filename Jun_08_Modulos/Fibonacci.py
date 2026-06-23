def fibonacci(n):
    if (n == 1):
        return(0)
    elif (n == 2):
        return(1)
    else:
        f1 = 0 # primeiro termo
        f2 = 1 # segundo termo
        for i in range(3, n+1):
            f3 = f2 + f1 # terceiro termo = primeiro termo + segundo termo
            
            f1 = f2
            f2 = f3
            
        return(f3)
    
# módulo principal
for n in range(1, 21):
    print(f"{fibonacci(n)}, ", end="")
        
            