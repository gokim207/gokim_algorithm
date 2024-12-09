import math
n,a,b,c = map(int,input().split())
print(math.comb(n,a)*math.comb(n-a,b)*math.comb(n-a-b,c))