n = int(input())
unwash = [i for i in range(n, 0, -1)]
washed = []
dried = []

while 1:
    x,y = map(int,input().split())
    for i in range(y):
        if x == 1:
            washed.append(unwash.pop())
        else:
            dried.append(washed.pop())
    if len(dried) == n:
        break
    
for i in washed:
    dried.append(i)
print(*dried[::-1], sep='\n')