s = input("Informe uma String: ")

print()

ctMaius = ctMinus = 0
n = len(s)
for i in range(n):
    if ((s[i] >= 'A') and (s[i] <= 'Z')):
        ctMaius += 1
    elif ((s[i] >= 'a') and (s[i] <= 'z')):
        ctMinus += 1

print('Maiúsculas =', ctMaius)
print('Minúsculas =', ctMinus)
