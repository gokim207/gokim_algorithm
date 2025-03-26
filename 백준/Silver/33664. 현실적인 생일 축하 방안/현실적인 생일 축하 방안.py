b,n,m = map(int,input().split())
present = {}
for i in range(n):
    x,y = input().split()
    present[x] = int(y)

result = 0
for i in range(m):
    x = input()
    result += present[x]

if result <= b:
    print('acceptable')
else:
    print('unacceptable')