a = input()
for i in a:
    if i == 'I':
        print('E',end="")
    elif i == 'E':
        print('I',end="")
    elif i == 'S':
        print('N', end="")
    elif i == 'N':
        print('S',end="")
    elif i == 'F':
        print('T',end="")
    elif i == 'T':
        print('F',end="")
    elif i == 'P':
        print('J')
    else:
        print('P')