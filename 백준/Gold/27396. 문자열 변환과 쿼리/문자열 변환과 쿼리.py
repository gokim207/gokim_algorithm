import sys
input = sys.stdin.readline
a,b = input().split()

for i in range(int(b)):
    x = input().split()
    if x[0] == '1':
        if x[1] == x[2] or x[1] not in a:
            continue
        a = a.replace(x[1],x[2], a.count(x[1]))
        continue
    print(a)