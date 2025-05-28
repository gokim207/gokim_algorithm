import sys
input = sys.stdin.readline
n,b,c = map(int,input().split())
x = list(map(int,input().split())) + [0,0]
result = 0

def three(i):
    global result
    min1 = min(x[i:i+3])
    result += (b+(2*c)) * min1
    x[i] -= min1
    x[i+1] -= min1
    x[i+2] -= min1

def two(i):
    global result
    min1 = min(x[i:i+2])
    result += (b+c) * min1
    x[i] -= min1
    x[i+1] -= min1

def one(i):
    global result
    result += b * x[i]

for i in range(len(x)-2):
    if b < c:
        one(i)
    elif x[i+1] > x[i+2]:
        min1 = min(x[i], x[i+1]-x[i+2])
        x[i] -= min1
        x[i+1] -= min1
        result += (b+c)*min1
        three(i)
        one(i)
    else:
        three(i)
        two(i)
        one(i)

print(result)