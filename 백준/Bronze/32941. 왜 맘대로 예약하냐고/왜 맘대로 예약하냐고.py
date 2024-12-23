t,x = map(int,input().split())
n = int(input())
d = [0]*t
for i in range(n):
    m = int(input())
    a = list(map(int,input().split()))
    for j in a:
        d[j-1] += 1

if d[x-1] == n:
    print('YES')
    exit()
print('NO')