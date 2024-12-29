a,b = map(int,input().split())
c,d = map(int,input().split())

result = (a+b+c+d - 1)%4
if result == 0:
    print(4)
else:
    print(result)