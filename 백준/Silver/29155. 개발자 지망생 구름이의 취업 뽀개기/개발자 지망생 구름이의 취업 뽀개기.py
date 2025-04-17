n = int(input())
d = [[], [], [], [], []]
a = list(map(int,input().split()))

def cal(a, d, n):
    global result
    
    for i in range(a):
        if i == 0:
            result += d[n][i]
        else:
            result += d[n][i] + (d[n][i] - d[n][i-1])

for i in range(n):
    k, l = map(int,input().split())
    if k == 1:
        d[0].append(l)
    elif k == 2:
        d[1].append(l)
    elif k == 3:
        d[2].append(l)
    elif k == 4:
        d[3].append(l)
    else:
        d[-1].append(l)
d[0].sort()
d[1].sort()
d[2].sort()
d[3].sort()
d[4].sort()

result = 0
for i in range(5):
    cal(a[i], d, i)
print(result + 240)