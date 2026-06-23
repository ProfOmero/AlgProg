n = 7
a = [0] * n

for i in range(n):
    a[i] = int(input())
    
b = [0] * n
for i in range(n):
    b[i] = a[i] * 2
    
for i in range(n):
    print(f"A[{i}] = {a[i]:2}   B[{i}] = {a[i]:2} X 2 = {b[i]:2}")