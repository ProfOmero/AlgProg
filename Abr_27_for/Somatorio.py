n = int(input("Quantos valores? "))

print()

sm = 0 # variável do tipo somatório

for i in range(1, n+1):
    vlr = int(input(f"{i}o. valor: "))
    
    sm = sm + vlr
    
print()
print("Soma dos valores =", sm)
    