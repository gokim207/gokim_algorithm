import math
a = list(map(int,input().split()))
result = 10**7

for i in range(5):
    for j in range(i+1, 5):
        for k in range(j+1, 5):
            result = min(result, math.lcm(math.lcm(a[i],a[j]),a[k]))
print(result)