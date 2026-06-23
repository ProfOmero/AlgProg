n = int(input("n: "))

print()

if (n < 0):
    print(f"{n} é NEGATIVO")
else:    
    if (n == 0):
        print(f"{n} é NEUTRO")
    else:
        print(f"{n} é POSITIVO")
