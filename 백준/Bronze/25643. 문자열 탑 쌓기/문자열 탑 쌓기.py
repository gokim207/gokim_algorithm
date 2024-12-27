n,m = map(int,input().split())
str = []

for i in range(n):
    str.append(input())

for i in range(n-1):
    x = str[i]
    y = str[i+1]
    
    check = False
    for j in range(1, m+1):
        if x[m-j:] == y[:j] or x[:j] == y[m-j:]:
            check = True
            break 
    if not check:
        print(0)
        exit()
print(1)