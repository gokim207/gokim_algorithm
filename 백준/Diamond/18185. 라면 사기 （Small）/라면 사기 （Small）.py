import sys
input = sys.stdin.readline
n = int(input())
x = list(map(int,input().split())) + [0,0]
result = 0

def three(i):
    global result
    min1 = min(x[i:i+3])
    result += 7 * min1
    x[i] -= min1
    x[i+1] -= min1
    x[i+2] -= min1

def two(i):
    global result
    min1 = min(x[i:i+2])
    result += 5 * min1
    x[i] -= min1
    x[i+1] -= min1

def one(i):
    global result
    result += 3 * x[i]

for i in range(len(x)-2):
    if x[i+1] > x[i+2]:
        min1 = min(x[i], x[i+1]-x[i+2])
        x[i] -= min1
        x[i+1] -= min1
        result += 5*min1
        three(i)
        one(i)
    else:
        three(i)
        two(i)
        one(i)

print(result)
