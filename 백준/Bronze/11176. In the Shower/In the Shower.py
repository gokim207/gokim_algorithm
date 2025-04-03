for i in range(int(input())):
    e,n = map(int,input().split())
    result = 0
    for j in range(n):
        x = int(input())
        if x > e:
            result += 1
    print(result)