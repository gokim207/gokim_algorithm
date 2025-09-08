import collections

a=int(input())
d= collections.deque(i for i in range(1,a+1))
while True:
    if(len(d)==1):
        print(d[0])
        break
    else:
        d.popleft()
        b = d[0]
        d.popleft()
        d.append(b)