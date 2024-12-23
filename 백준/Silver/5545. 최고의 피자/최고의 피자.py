import math
n = int(input())
a,b = map(int,input().split())
c = int(input())
d = []
result = c / a
kcal = c
count = 1

for i in range(n):
    d.append(int(input()))    
d.sort(reverse=True)

for i in d:
    kcal += i
    price = kcal / (a + b*count)
    result = max(result, price)
    count += 1

print(math.floor(result))
