for i in range(int(input())):
    x,y = map(int,input().split())
    if x > y:
        inner = abs(x-y)
        outer = 43 - inner
    else:
        outer = abs(x-y)
        inner = 43 - outer
        
    if inner > outer:
        print('Inner circle line')
    else:
        print('Outer circle line')