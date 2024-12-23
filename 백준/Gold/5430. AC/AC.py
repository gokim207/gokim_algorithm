import collections
import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    p = input().rstrip()
    m = int(input())
    x = input().rstrip()[1:-1]
    spin = False
    
    try:
        if m != 0:
            x = collections.deque(map(int,x.split(',')))
        else:
            x = collections.deque()
        
        for j in p:
            if j == 'R':
                if spin:
                    spin = False
                else:
                    spin = True
            else:
                if spin:
                    x.pop()
                else:
                    x.popleft()
            
        if spin:
            x.reverse()
        print('[',end="")
        for i in range(len(x)):
            if i != len(x)-1:
                print(x[i],end=",")
            else:
                print(x[i],end="")
        print(']')
    except:
        print('error')