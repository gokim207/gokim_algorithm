import math

ppi = []
for i in range(int(input())):
    x,y = map(int,input().split())
    ppi.append([i+1, math.sqrt(x**2 + y**2)/77])

ppi.sort(key=lambda ppi: (-ppi[1], ppi[0]))
for i in ppi:
    print(i[0])