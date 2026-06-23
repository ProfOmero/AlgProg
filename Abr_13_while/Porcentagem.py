n = int(input("Quantos números inteiros serão informados? "))
        
print()

ctPares = 0

i = 1
while (i <= n):
    nro = int(input(f"{i}o. número: "))
    
    if ((nro % 2) == 0):
        ctPares = ctPares + 1
    
    i = i + 1

porcemPares = 0

ctImpares = 0
porcemImpares = 0
if (n != 0):
    porcemPares = (ctPares / n) * 100
    
    ctImpares = n - ctPares
    porcemImpares = 100 - porcemPares
    
print()
print(f"Existem {ctPares} pares ({porcemPares:.2f}%)")
print(f"Existem {ctImpares} ímpares ({porcemImpares:.2f}%)")
    
