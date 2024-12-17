n,m = map(int,input().split())
a = list(map(int,input().split()))

for i in a:
    if i%2 == 0:
        n -= (i//2)
    else:
        n -= (i//2) + 1

if n <=0 :
    print('YES')
else:
    print('NO')