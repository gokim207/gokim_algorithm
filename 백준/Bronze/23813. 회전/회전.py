n = input()
result = 0
x = n

while 1:
    if len(x) == 1:
        print(x)
        exit()
    
    x = x[-1] + x[:-1]
    
    result += int(x)
    if x == n:
        print(result)
        exit()