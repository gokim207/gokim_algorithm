import math
for i in range(int(input())):
    x = input()
    d = []
    x_sqrt = int(math.sqrt(len(x)))
    for j in range(x_sqrt):
        y = x[j*x_sqrt:j*x_sqrt+x_sqrt]
        d.append(y)
        
    for j in range(x_sqrt):
        y = ''
        for k in range(len(d)):
            y += d[k][-j-1]
        print(y,end="")
    print()