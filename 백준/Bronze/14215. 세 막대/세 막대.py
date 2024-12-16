a,b,c = map(int,input().split())
num = [a,b,c]
num.sort()
if num[0] + num[1] <= num[2]:
    print((num[0]+num[1]+(num[0]+num[1]-1)))
else:
    print(sum(num))