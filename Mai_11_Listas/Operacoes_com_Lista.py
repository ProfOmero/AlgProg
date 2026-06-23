n = int(input()) # lendo o tamanho da lista

a = [0] * n

for i in range(n):
    a[i] = int(input())
    
print(a)
print("Soma  = ", sum(a))
print("Média = ", sum(a) / len(a))
print("Menor = ", min(a))
print("Maior = ", max(a))

