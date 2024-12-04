n = int(input())
a = list(map(int,input().split()))
for i in range(len(a)):
    for j in range(len(a)):
        for k in range(len(a)):
            if i == j or j == k or i == k:
                continue
            result = list(str((a[i]-a[j])/a[k]))
            if len(result[result.index('.')+1:]) != 1:
                print('no')
                exit()
print('yes')