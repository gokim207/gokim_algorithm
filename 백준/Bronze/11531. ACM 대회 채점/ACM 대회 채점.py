result = 0
time = 0
wrong = []
while 1:
    x = input().split()
    if x[0] == '-1':
        break
    if x[-1] == 'right':
        result += 1
        time += 20*(wrong.count(x[1])) + int(x[0])
    else:
        wrong.append(x[1])
print(result, time)