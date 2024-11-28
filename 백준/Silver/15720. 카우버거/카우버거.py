n,m,k = map(int,input().split())
ham = list(map(int,input().split()))
side = list(map(int,input().split()))
drink = list(map(int,input().split()))

saleResult = 0
notSaleResult = sum(ham) + sum(side) + sum(drink)

ham.sort(reverse=True)
side.sort(reverse=True)
drink.sort(reverse=True)

min1 = min(n,m,k)
for i in range(min1):
    saleResult += (ham[0] + side[0] + drink[0])*0.9
    ham.pop(0)
    side.pop(0)
    drink.pop(0)

print(notSaleResult)
print(int(saleResult) + sum(ham) + sum(side) + sum(drink))