n = int(input())
count = 0

for i in range(1, n+1):
    for j in range(i, n//i+1):
        count += 1
print(count)
