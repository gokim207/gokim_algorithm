n = int(input())
a = list(map(int,input().split()))
a.append(0)
result = 0
first = 0
count = 0
before = 0
for i in range(n+1):
    if first == 0:
        first = a[i]
        before =  a[i]
    elif before < a[i]:
        count +=1
    else:
        if count != 0:
            result = max(result, a[i-1] - first)
        count = 0
        first = a[i]
    before = a[i]
print(result)