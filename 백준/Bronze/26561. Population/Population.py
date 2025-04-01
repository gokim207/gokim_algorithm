for i in range(int(input())):
    x,y = map(int,input().split())
    print(x - (y//7) + (y//4))