import collections
n = int(input())
a=  list(map(int,input().split()))
a.reverse()
result = collections.deque()

for i in range(n):
    if a[i] == 1:
        result.appendleft(i+1)
    elif a[i] == 2:
        result.insert(1, i+1)
    else:
        result.append(i+1)
print(*result)