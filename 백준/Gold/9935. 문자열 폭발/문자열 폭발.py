import sys
input = sys.stdin.readline
a = input().strip()
b = list(input().strip())
stack = []
lenght = len(b)
for i in a:
    stack.append(i)
    if stack[len(stack)-lenght:len(stack)] == b:
        for _ in range(lenght):
            stack.pop()

if stack:
    print(*stack,sep="")
else:
    print('FRULA')
