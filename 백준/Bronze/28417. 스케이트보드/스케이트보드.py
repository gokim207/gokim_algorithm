result = []
for i in range(int(input())):
    track = list(map(int,input().split()))
    a = track[:2]
    b = track[2:]
    total = max(a) + max(b)
    b.remove(max(b))
    total += max(b)
    result.append(total)
print(max(result))