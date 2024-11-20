cho = 72
han = 73.5

a = list(map(int,input().split()))
b = list(map(int,input().split()))
d = [13, 7, 5, 3, 3, 2]
count = [2, 2, 2, 2, 2, 5]

for i in range(len(a)):
    cho -= (count[i] - a[i]) * d[i]
    
for i in range(len(b)):
    han -= (count[i] - b[i]) * d[i]

if cho < han:
    print('ekwoo')
else:
    print('cocjr0208')