d = []
for i in range(int(input())):
    a = int(input())
    if a == 0:
      d.pop()
    else:
      d.append(a)
      
print(sum(d))