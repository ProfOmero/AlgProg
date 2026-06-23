s = input("Informe uma String: ")

print()

n = len(s)
for i in range(n):
    for j in range(i+1):
        print(s[j], end=" ")
    print()