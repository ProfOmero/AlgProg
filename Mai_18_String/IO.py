s = input("Informe uma String: ")

print()

# 1a. forma: mostrando a String de uma única vez
print(s)

# 2a. forma: mostrando caractere por caractere (for - each)
for item in s:
    print(item, end=" ")
    
print()

# 3a. forma: mostrando caractere por caractere (usando índice)
n = len(s)
for i in range(n):
    print(s[i], end=" ")

print()

