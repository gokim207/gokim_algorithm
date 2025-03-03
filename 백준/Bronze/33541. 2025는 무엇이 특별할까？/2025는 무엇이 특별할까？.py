n = int(input())+1
for i in range(n, 10000):
    j = str(i)
    if (int(j[:2]) + int(j[2:]))**2 == i:
        print(i)
        exit()
print(-1)