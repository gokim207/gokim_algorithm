a = list(map(int,input().split()))
b = list(map(int,input().split()))

result = 0
for i in range(len(a)):
    if a[i] < b[i]:
        result += b[i] - a[i]
print(result)