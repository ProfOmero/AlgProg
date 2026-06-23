binario = input("Valor na base binária = ")

posicao = len(binario) - 1

decimal = 0

for item in binario:
    if (item == '1'):
        decimal = decimal + (2 ** posicao)
        
    posicao = posicao - 1
    

print()
print(f"{binario} = {decimal}")
        