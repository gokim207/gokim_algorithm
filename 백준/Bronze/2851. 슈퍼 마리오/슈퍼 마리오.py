total = 0
over_100 = 0
for i in range(10):
    x = int(input())
    if total + x > 100:
        over_100 = total + x
        break
    else:
        total += x
if abs(100 - total) < abs(100 - over_100):
    print(total)
elif abs(100-total) > abs(100 - over_100):
    print(over_100)
else:
    print(over_100)