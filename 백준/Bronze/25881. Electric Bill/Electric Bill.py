n,m = map(int,input().split())
for i in range(int(input())):
    x = int(input())
    if x > 1000:
        y = (x - 1000)*m
        print(x,1000*n+y)
    else:
        print(x, x*n)