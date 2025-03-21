p,q = map(int,input().split())
a,b = map(int,input().split())


if p > q:
    print(q*a)
else:
    print((p*a) + (q-p)*b)