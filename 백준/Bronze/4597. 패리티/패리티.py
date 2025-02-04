while 1:
    a = input()
    if a == '#':
        break
    
    one = 0
    
    for i in a:
        if i == 'e':
            num = True
        elif i == 'o':
            num = False
        elif i == '1':
            one += 1
            print(i,end = "")
        else:
            print(i,end = "")
            
    if num:
        if one%2 == 0:
            print(0)
        else:
            print(1)
    else:
        if one%2 == 0:
            print(1)
        else:
            print(0)