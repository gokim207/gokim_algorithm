a, b, c, d = map(int, input().split())
li = list(map(int, input().split()))
for n in li:
    attacked = 0
    if 0 < n % (a+b) <= a:
        attacked += 1
    if 0 < n % (c+d) <= c:
        attacked += 1
    print(attacked)