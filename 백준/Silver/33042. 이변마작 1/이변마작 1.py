n = int(input())
a = list(input().split())
man = [0]*9
tong = [0]*9
sa = [0]*9
za = [0]*7

for i in range(len(a)):
    if a[i][-1] == 'm':
        man[int(a[i][0])-1] += 1
        if man[int(a[i][0])-1] > 4:
            print(i+1)
            exit()
    elif a[i][-1] == 'p':
        tong[int(a[i][0])-1] += 1
        if tong[int(a[i][0])-1] > 4:
            print(i+1)
            exit()
    elif a[i][-1] == 's':
        sa[int(a[i][0])-1] += 1
        if sa[int(a[i][0])-1] > 4:
            print(i+1)
            exit()
    else:
        za[int(a[i][0])-1] += 1
        if za[int(a[i][0])-1] > 4:
            print(i+1)
            exit()

print(0)