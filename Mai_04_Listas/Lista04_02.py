n = 7
a = [0] * n

for i in range(n):
    a[i] = int(input())
    
ctPares = ctImpares = 0
for i in range(n):
    print(f"x[{i}] = {a[i]:2}")
    
    if ((a[i] % 2) == 0):
        ctPares = ctPares + 1
    else:
        ctImpares = ctImpares + 1
        
porcemP = (ctPares / n) * 100
porcemI = (ctImpares / n) * 100

print()
print(f"Existem {ctPares} pares..: {porcemP:.2f}%")
print(f"Existem {ctImpares} impares: {porcemI:.2f}%")






