def digaOla():
    print("Olá!!!")
    
def digaOlaPara(nome):
    print("Olá Sr(a).", nome)
    
def boasVindas(nome, sexo):
    if ((sexo == 'm') or (sexo == 'M')):
        print("Olá Sr.", nome)
    else:
        print("Olá Sra.", nome)
    

# módulo principal (main)
digaOla() # sem utilizar parâmetros
print()
digaOlaPara("Juca Bala")
digaOlaPara("Maria do Socorro")
print()
boasVindas("Juca Bala", "M")
boasVindas("Maria do Socorro", "F")
