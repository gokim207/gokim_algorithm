while 1:
    x = int(input())
    if x == -1:
        break
    result = 0
    d = []
    for i in range(1,x//2+1):
        if x%i == 0:
            result += i
            d.append(i)
    if result == x:
        print(f'{x} = ',end="")
        for i in range(len(d)-1):
            print(d[i],end=" + ")
        print(d[-1])
    else:
        print(f'{x} is NOT perfect.')