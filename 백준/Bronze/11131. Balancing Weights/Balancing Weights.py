for i in range(int(input())):
    n = int(input())
    x = list(map(int,input().split()))
    if sum(x) <0:
        print('Left')
    elif sum(x) == 0:
        print('Equilibrium')
    else:
        print('Right')