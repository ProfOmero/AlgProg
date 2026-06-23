s = input()

n = len(s)

ct = 0
for item in s:
    if ((item >= '0') and (item <= '7')):
        ct = ct + 1

print(f"Tamanho da String = {n}.")
if (ct == n):
    print("Trata-se de uma sequencia octal.")
else:
    print(f"Existem {n-ct} caracteres que \"nao\" sao octais: de 0 ate 7.")
    