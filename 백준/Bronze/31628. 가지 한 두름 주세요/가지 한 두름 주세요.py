d = []
for i in range(10):
    d.append(list(input().split()))

for i in range(10):
    if len(set(d[i])) == 1:
        print(1)
        exit()
    x = [0] *10
    
    for j in range(10):
        x[j] = d[j][i]
    if len(set(x)) == 1:
        print(1)
        exit()
        
print(0)