a = [int(item) for item in input().split(" ")]

print()

n = len(a)

print("[", end="")
for i in range(n):
    print(f"{a[i]}", end="")
    if (i != (n-1)):
        print(", ", end="")
print("]")

print(a)
     

