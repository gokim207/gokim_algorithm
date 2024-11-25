for i in range(3):
    x = int(input())
    if i == 0 and (x != 3 and x != 1):
        print('EI')
        exit()
    elif i == 1 and (x != 6 and x!= 8):
        print('EI')
        exit()
    elif i == 2 and  x!=5 and x!= 2:
        print('EI')
        exit()
print('JAH')