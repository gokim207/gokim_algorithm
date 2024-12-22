import math
import sys
input = sys.stdin.readline
r,k,m = map(int,input().split())
t = math.floor(m/k)
print(math.floor(r>>t))