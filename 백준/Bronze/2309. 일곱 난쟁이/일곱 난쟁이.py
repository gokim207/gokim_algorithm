d = []
for i in range(9):
    d.append(int(input()))
d.sort()
total = sum(d)
result = 0
check = False
for i in range(9):
    for j in range(i+1, 9):
        if total - d[i] - d[j] == 100:
            d.pop(i)
            d.pop(j-1)
            check = True
            break
    if check:
        for j in d:
            print(j)
        break