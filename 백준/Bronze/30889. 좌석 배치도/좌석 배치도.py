d = [['.']*20 for _ in range(10)]

for i in range(int(input())):
    a = input()
    x = ord(a[0])-65
    d[x][int(a[1:])-1] = 'o'

for i in d:
    for j in i:
        print(j,end="")
    print()