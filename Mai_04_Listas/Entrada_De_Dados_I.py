n = int(input("Quantos itens na lista? "))

print()

a = [0] * n

for i in range(n):
    a[i] = int(input(f"{i+1}o. item = "))
    

print()
print(a)