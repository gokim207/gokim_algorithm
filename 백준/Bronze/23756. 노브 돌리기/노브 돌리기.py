n = int(input())
node = int(input())
result = 0

for i in range(n):
    x = int(input())
    if node < x:
        result += min(abs(node-x), node+(360-x))
    else:
        result += min(abs(node-x), (360-node)+x)
    node = x
print(result)