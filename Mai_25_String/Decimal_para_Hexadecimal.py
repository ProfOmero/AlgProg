decimal = int(input("Valor na base decimal = "))

n = decimal

if (decimal == 0):
    hexadecimal = '0'
else:
    base = '0123456789ABCDEF'
    hexadecimal = ''
    while (decimal != 0):
        hexadecimal = base[decimal % 16] + hexadecimal
        
        decimal = decimal // 16
        
print()
print(f"{n} = {hexadecimal}")
        