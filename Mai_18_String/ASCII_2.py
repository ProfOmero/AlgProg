for i in range(65, 91):
    print(chr(i), chr(i+32), sep="", end=" ")
    
print()

for i in range(97, 123):
    print(chr(i), chr(i-32), sep="", end=" ")
    
print()
print()

for i in range(48, 58):
    print(i, ": ", chr(i), sep="")