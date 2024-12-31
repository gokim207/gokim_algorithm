for i in range(int(input())):
    x = int(input())
    a = list(map(int,input().split()))
    even = 0
    odd = 0
    for j in a:
        if j%2 == 0:
            even += 1
        else:
            odd += 1
    
    
    if even == odd:
        print('heeda0528')
    elif max(odd, even)%2 == 0:
        print('heeda0528')
    else:
        print('amsminn')