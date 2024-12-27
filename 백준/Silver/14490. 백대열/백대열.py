import math
n,m = map(int,input().split(':'))
if math.gcd(n,m) != 1:
    n,m = n // math.gcd(n,m), m // math.gcd(n,m)
print(n,m,sep=":")