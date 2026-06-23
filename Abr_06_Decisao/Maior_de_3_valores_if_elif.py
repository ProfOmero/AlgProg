a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

print()

if ((a >= b) and (a >= c)):
    print(a, "é o maior")
elif (b >= c):
    print(b, "é o maior")
else:
    print(c, "é o maior")
    
print("\n<<< fim do programa >>>")