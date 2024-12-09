m = int(input())
n = int(input(),2)
k = int(input())

if n % (2**k) == 0:
    print('YES')
else:
    print('NO')