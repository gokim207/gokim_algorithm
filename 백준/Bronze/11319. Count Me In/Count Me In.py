d = ['a', 'e' ,'o', 'i', 'u']
for i in range(int(input())):
    x = input().lower()
    result = [0,0]
    for i in x:
        if i == ' ':
            continue
        elif i in d:
            result[1] +=1
        else:
            result[0] += 1
    print(*result)