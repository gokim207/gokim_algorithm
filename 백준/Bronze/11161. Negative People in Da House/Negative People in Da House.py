for i in range(int(input())):
    min1 = 0
    now = 0
    for j in range(int(input())):
        x,y = map(int,input().split())
        now = now + x -y
        min1 = min(min1, now)
    print(-min1)