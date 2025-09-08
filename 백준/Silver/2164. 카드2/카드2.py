import collections

a = int(input())
d = collections.deque(i for i in range(1, a+1))

for i in range(a-1):
    d.popleft()
    d.append(d.popleft())
print(d[0])