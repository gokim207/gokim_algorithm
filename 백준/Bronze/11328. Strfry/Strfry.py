for i in range(int(input())):
    x,y = input().split()
    if len(x) != len(y):
        print('Impossible')
        continue
    x = list(x)
    y = list(y)
    check = True
    for i in y:
        if x.count(i) != y.count(i):
            print('Impossible')
            check = False
            break
    if check:
        print('Possible')