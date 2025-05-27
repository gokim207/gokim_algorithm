n = int(input())
a = n//5
b = (n - (n//5)*5)//3

if a*5 + b*3 == n:
    print(a+b)
else :
    n -= (a*5) + (b*3)
    while a > 0:
        a -= 1
        n += 5
        if n%3 == 0:
            b += n//3
            n = 0
            print(a+b)
            exit()
    print(-1)