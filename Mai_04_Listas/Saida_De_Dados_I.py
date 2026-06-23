n = int(input("Quantos itens tem na lista? "))

print()

a = [0] * n # declaração da lista "a" com "n" itens

for i in range(n):
    a[i] = int(input(f"{i+1}o. item = "))
    
print()

# 1a. forma: print da lista
print(a)
print()

# 2a. forma: usando um for-each
for item in a:
    print(item, end=" ")
    
print()
print()

# 3a. forma: mostrando os itens das posições da lista
for i in range(n):
    print(a[i], end=" ")
    
print()


    

