while 1:
    x = list(input().lower().split())
    if x[0] == '*':
        break
    y = x[0][0]
    for i in x:
        if i[0] != y:
            y = True
            break
    if y == True:
        print('N')
    else:
        print('Y')