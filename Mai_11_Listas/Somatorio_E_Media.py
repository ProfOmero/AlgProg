n = int(input()) # lendo o tamanho da lista

a = [0] * n

for i in range(n):
    a[i] = int(input())
    
# somatório dos 'n' valores da lista 'a'
soma = 0
for i in range(n):
    soma = soma + a[i]
    
media = 0
if (n != 0): # verificando a divisão por zero
    media = soma / n
    
print(a)
print("Soma  = ", soma)
print("Média = ", media) 