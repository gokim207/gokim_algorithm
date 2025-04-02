for i in range(int(input())):
    x = input().strip()
    if x == ' ' or x == '':
        print('invalid input')
        continue
    y= True
    a = ''
    for j in x:
        if not j.isdigit():
            print('invalid input')
            y = False
            break
        else:
            a += j
    if y:
        print(int(a, 10))