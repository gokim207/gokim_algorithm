import sys
input = sys.stdin.readline
n = input()
a = list(map(int,input().split()))
sum_a = sum(a) * -1
a.sort()
for i in range(len(a)):
    if a[i] >= sum_a:
        print(sum_a*-1)
        exit()
    a[i] = sum_a
    sum_a = sum(a) * -1
print(sum_a*-1)