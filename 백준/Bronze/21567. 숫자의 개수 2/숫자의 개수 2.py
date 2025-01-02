total = 1
for i in range(3):
    total *= int(input())
d = [0]*10

for i in str(total):
    d[int(i)] += 1

for i in d:
    print(i)