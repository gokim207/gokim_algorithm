h,w = map(int,input().split())
c,d = map(int,input().split())
count = 1
W = w
map = [0 for _ in range(h)]
for i in range(1, h):
    map[i] = i
    if i> w:
        print(-1)
        exit()
    d -= i
    if d < 0:
        print(-1)
        exit()
    
for i in range(h-1, -1, -1):
    value = min(d, W - map[i])
    d -= value
    map[i] += value
    W -= 1
    
if d > 0:
    print(-1)
    exit()
    
for i in range(h):
    for j in range(w):
        if map[i] > j:
            print(9,end=" ")
        else:
            print(1,end=" ")
    print()