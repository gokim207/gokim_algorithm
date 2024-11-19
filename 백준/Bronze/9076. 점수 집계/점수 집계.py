for i in range(int(input())):
    x = list(map(int,input().split()))
    check = False
    x.sort()
    for i in x[1:-1]:
        
        if abs(i-x[1]) >=4 or abs(i-x[-2]) >= 4:
            print('KIN')
            check = True
            break
    if not check:
        print(sum(x) - x[0] - x[-1])