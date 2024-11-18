n,m = map(int,input().split())
a = list(map(int,input().split()))
stress = 0
result = 0

for i in a:
    stress += i
    if stress < 0:
        stress = 0
    if stress >= m:
        result += 1
print(result)