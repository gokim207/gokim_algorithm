alpha = [chr(i) for i in range(65,65+26)]
for i in range(int(input())):
    x,y = input().split()
    if y == 'C':
        a = list(input().split())
        for j in a:
            print(alpha.index(j)+1,end=" ")
    else:
        a = list(map(int,input().split()))
        for j in a:
            print(alpha[j-1],end=" ")
    print()