t,f,n = map(int,input().split())
table = [0, 0]

for i in range(n+1):
    x = t + i
    y = f + (n-i)
    if x %3 == 0 and y %4 == 0:
        print(x//3,y//4)
        exit()

print(-1)