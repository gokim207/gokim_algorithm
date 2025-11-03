n = int(input())

for i in range(1, n):
  x = str(i)
  total = i
  for j in x:
    total += int(j)
  if n == total:
    print(i)
    exit()
  
print(0)