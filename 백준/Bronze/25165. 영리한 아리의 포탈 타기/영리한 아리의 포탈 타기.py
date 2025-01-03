n,m = map(int,input().split())
x,d = map(int,input().split())
c,r = map(int,input().split())

if d == 0:
    if n%2 == 0:
        print('NO...')
    else:
        if c == n:
            print('YES!')
        else:
            print('NO...')
else:
    if n%2 == 0:
        if c == n:
            print('YES!')
        else:
            print('NO...')
    else:
        print('NO...')