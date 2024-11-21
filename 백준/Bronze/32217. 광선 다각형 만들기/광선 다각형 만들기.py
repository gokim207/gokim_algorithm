n = int(input())
a_sum = 180*(n-1)
a = list(map(int,input().split()))
for i in a:
    a_sum -= i*2
print(a_sum)