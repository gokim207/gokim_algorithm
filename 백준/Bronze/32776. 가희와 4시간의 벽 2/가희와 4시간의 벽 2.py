n = int(input())
a1,f,a2 = map(int,input().split())

if n <= 4*60 or n <= a1+f+a2:
    print('high speed rail')
else:
    print('flight')