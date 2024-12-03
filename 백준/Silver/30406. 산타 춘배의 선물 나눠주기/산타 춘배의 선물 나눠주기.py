n = int(input())
a = list(map(int,input().split()))
count = [a.count(0), a.count(1), a.count(2), a.count(3)]
b = min(count[0],count[-1])
c = min(count[1],count[2])
result = 3*(min(count[0],count[-1])) + 3*(min(count[1], count[2]))
check = []
count[0] -= b
count[1] -= c
count[2] -= c
count[3] -= b

if count[0] != 0 and count[1] != 0:
    result += (0^1)*min(count[0],count[1])
elif count[0] != 0 and count[2] != 0:
    result += (0^2)*min(count[0],count[2])
elif count[-1] != 0 and count[1] != 0:
    result += (3^1)*min(count[3],count[1])
elif count[-1] != 0 and count[2] != 0:
    result += (3^2)*min(count[3],count[2])
    
print(result)

'''
0,3
1,2
2,1
3,0

0011
1010
'''