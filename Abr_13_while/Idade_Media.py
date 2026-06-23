n = int(input("Quantas idades serão informadas? "))

print()

smIdade = 0
idadeMd = 0

i = 1
while (i <= n):
    idade = int(input(f"{i}a. idade: "))
    
    smIdade = smIdade + idade  
    
    i = i + 1
    
if (n != 0):
    idadeMd = smIdade / n
    
print()    
print(f"Idade média = {idadeMd:.2f}")
