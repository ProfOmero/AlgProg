def matriz(n):
    for i in range(n):
        for j in range(n):
            # primeira linha e última linha
            if ((i == 0) or (i == (n-1))):
                print("* ", end="")
            # primeira coluna e última coluna
            elif ((j == 0) or (j == (n-1))):
                print("* ", end="")
            else:
                print("@ ", end="")
        print()

# módulo principal
n = int(input("Tamanho da matriz quadrada? "))

matriz(n)
                
                  