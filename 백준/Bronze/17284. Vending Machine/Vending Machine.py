money = 5000
a = list(map(int,input().split()))
for i in a:
    if i == 1:
        money -= 500
    elif i == 2:
        money -= 800
    else:
        money -= 1000
print(money)