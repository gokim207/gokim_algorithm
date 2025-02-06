import sys
input = sys.stdin.readline
for i in range(int(input())):
    x = input().strip()
    count = 0
    
    while 1:
        if x == '6174':
            print(count)
            break
        
        d = [0 for _ in range(10)]
        for i in str(x):
            d[int(i)] += 1
        
        small = ''
        for i in range(10):
            for j in range(d[i]):
                small += str(i)
        big = small[::-1]
        x = str(int(big) - int(small))
        
        if len(x) != 4:
            for i in range(4-len(x)):
                x = '0' + x
        count += 1    