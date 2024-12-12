import collections
a = input()
b = list(input())
stack = collections.deque()
result = 0
for i in a:
    stack.append(i)
    if len(stack) == len(b):
        if list(stack) == b:
            result += 1
        stack.popleft()
print(result)