n = int(input()) # lendo o tamanho da lista

a = [0] * n

for i in range(n):
    a[i] = int(input())
    
menor = a[0]
maior = a[0]
for i in range(1, n):
    if (a[i] < menor):
        menor = a[i]
    else:
        if (a[i] > maior):
            maior = a[i]
            
print(a)
print("Menor = ", menor)
print("Maior = ", maior)