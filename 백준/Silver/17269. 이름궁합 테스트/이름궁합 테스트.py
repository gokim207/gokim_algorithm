import collections
count = {'A' : 3, 'B': 2, 'C': 1, 'D' : 2, 'E': 4, 'F': 3, 'G':1, 'H': 3, 'I':1, 'J': 1, 'K':3, 'L':1, 'M':3, 'N':2, 'O':1, 'P':2, 'Q':2, 'R':2, 'S':1, 'T':2, 'U':1, 'V':1, 'W':1, 'X':2,'Y':2, 'Z':1}
n,m = input().split()
a,b = input().split()
name = []
for i in range(min(len(a), len(b))):
    name.append(a[i])
    name.append(b[i])
    
if len(a) > len(b):
    for i in range(min(len(a),len(b)), len(a)):
        name.append(a[i])
elif len(a) < len(b):
    for i in range(min(len(a), len(b)), len(b)):
        name.append(b[i])

for i in range(len(name)):
    name[i] = count[name[i]]

while len(name) != 2:
    x = collections.deque()
    for i in range(len(name)-1):
        x.append((name[i] + name[i+1])%10)
    name = list(x)
if name[0] != 0:
    print(name[0],name[1], sep='',end="%")
else:
    print(name[1],end="%")