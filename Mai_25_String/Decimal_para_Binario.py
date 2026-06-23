decimal = int(input("Valor na base decimal: "))

n = decimal

if (decimal == 0):
    binario = '0'
else:
    binario = ''
    while (decimal != 0):
        binario = str(decimal % 2) + binario
        
        decimal = decimal // 2

print()
print(f"{n} = {binario}")