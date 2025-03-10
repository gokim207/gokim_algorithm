a = int(input())
b = int(input())

for i in range(b):
    a += 1
    if a > 24:
        a = 1

if a > 12:
    print(a-12)
else:
    print(a)