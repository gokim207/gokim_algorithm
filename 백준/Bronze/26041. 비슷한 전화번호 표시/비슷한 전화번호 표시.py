a = input().split()
b = input()
result = 0

for i in a:
    if len(i) < len(b) or i == b:
        continue
    if i[:len(b)] == b:
        result += 1
print(result)