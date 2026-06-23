n = int(input("Quantas idades serão informadas? "))

print()

smIdades = 0
mdIdades = 0

for i in range(1, n+1):
    idade = int(input(f"{i}a. idade: "))
    
    smIdades = smIdades + idade # somatório das idades
    
print()
if (n != 0):
    mdIdades = smIdades / n # definição da média
    
print("Soma das Idades =", smIdades)
print("Idade média     =", mdIdades)
    
    