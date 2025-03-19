n = int(input())
total = (n*(n**2 + 1))//2
square = []
check = []
l_cross = 0
r_cross = 0

for i in range(n):
    square.append(list(map(int,input().split())))
    
for i in range(n):
    count = 0
    if sum(square[i]) != total:
        print('FALSE')
        exit()
    
    for j in range(n):
        if square[j][i] in check:
            print('FALSE')
            exit()
        check.append(square[j][i])
        count += square[j][i]
        
    if count != total:
        print('FALSE')
        exit()
    
    l_cross += square[i][i]
    r_cross += square[i][-i-1]
    
if l_cross == r_cross == total:
    print('TRUE')
    exit()
print('FALSE')