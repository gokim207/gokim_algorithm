import sys
input = sys.stdin.readline

for i in range(int(input())):
    n,m,k = map(int,input().split())
    a = 1 + (k-1) *2
    if a >= n and a >= m:
        print('Yuto')
    else:
        if n%2 == 1 and m%2 == 1:
            print('Yuto')
        else:
            print('Platina')