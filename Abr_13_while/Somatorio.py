n = int(input("Quantos valores? "))

print()

sm = 0	# somatório

i = 1
while (i <= n):
    vlr = int(input(f"{i}o. valor: "))
    
    sm = sm + vlr
    i = i + 1
    
print()
print("Soma dos valores =", sm)