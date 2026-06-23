n = int(input("Quantos números inteiros serão informados? "))

print()

ctPares = 0 # variável do tipo contador

for i in range(1, n+1):
    nro = int(input(f"{i}o. valor: "))
    
    if ((nro % 2) == 0):
        ctPares = ctPares + 1 # realizando a contagem de pares
        
ctImpares = n - ctPares

porcemP = porcemI = 0
if (n != 0):
    porcemP = (ctPares / n) * 100		# calculando porcentagem
    porcemI = (ctImpares / n) * 100		# calculando porcentagem

print()
print(f"Existem {ctPares} números pares ({porcemP:.2f}%)")
print(f"Existem {ctImpares} números ímpares ({porcemI: .2f}%)")