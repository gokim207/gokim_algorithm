a = list(map(int,input().split()))
b = list(map(int,input().split()))
result = 0

for i in range(int(input())):
    x,y = map(int,input().split())
    if x == 1:
        if a[0] >= y*b[0] and a[1] >= y*b[1] and a[2] >= y*b[2] and a[3] >= y*b[3]:
            result += y
            print(result)
            a[0] -= y*b[0]
            a[1] -= y*b[1]
            a[2] -= y*b[2]
            a[3] -= y*b[3]
        else:
            print('Hello, siumii')
    elif x == 2:
        a[0] += y
        print(a[0])
    elif x == 3:
        a[1] += y
        print(a[1])
    elif x == 4:
        a[2] += y
        print(a[2])
    else:
        a[3] += y
        print(a[3])