import sys
input = sys.stdin.readline

for i in range(int(input())):
    a = list(input().strip().split(','))
    b = input().strip().split('|')
    result = 1000000000000
    d = {}
    
    for i in a:
        d[i[:i.index(":")]] = int(i[i.index(":")+1:])
    
    for i in b:
        x = i.split('&')
        y = 0
        for j in x:
            y  = max(y, d[j])
        result = min(result, y)
    print(result)