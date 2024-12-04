n = int(input())
d = {}
for i in range(n):
    x = input()
    x = x[x.index('.')+1:]
    if x not in d:
        d[x] = 1
    else:
        d[x] += 1

a = list(d.keys())
a.sort()
for i in a:
    print(i, d[i])