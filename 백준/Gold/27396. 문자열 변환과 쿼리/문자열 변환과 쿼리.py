a,b = input().split()
for i in range(int(b)):
    x = input().split()
    if x[0] == '2':
        print(a)
    else:
        a = a.replace(x[1], x[2])