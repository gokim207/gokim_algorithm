n,m = map(int,input().split())
x,d = map(int,input().split())
c,r = map(int,input().split())

if d == 0:
    if n%2 == 0:
        if c == 1 and r > x:
            print('YES!')
        else:
            print('NO...')
    else:
        if c == n or (c == 1 and r > x):
            print('YES!')
        else:
            print('NO...')
else:
    if n%2 == 0:
        if c == n or (c == 1 and r < x):
            print('YES!')
        else:
            print('NO...')
    else:
        if c == 1 and r < x:
            print('YES!')
        else:
            print('NO...')