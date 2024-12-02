import collections
n = int(input())
count = 1
stack = collections.deque()
result = []
for i in range(n):
    x = int(input())
    if count == x:
        result.append('+')
        result.append('-')
        count += 1
    elif count < x:
        while count != x+1:
            stack.append(count)
            result.append('+')
            count += 1
        result.append('-')
        stack.pop()
    elif x == stack[-1]:
        result.append('-')
        stack.pop()
    else:
        print('NO')
        exit()

for i in result:
    print(i)
