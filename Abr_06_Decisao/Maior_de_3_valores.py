a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

print()

if ((a >= b) and (a >= c)):
    print(a, "é o maior")
    
if ((b >= a) and (b >= c)):
    print(b, "é o maior")
    
if ((c >= a) and (c >= b)):
    print(c, "é o maior")
    
print("\n<<< fim do programa >>>")