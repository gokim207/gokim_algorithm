while 1:
    a = input()
    if a == '#':
        break
    
    first = 0
    for i in a:
        if i in 'aeiou':
            first = a.index(i)
            break
    
    if first == 0:
        print(a[:], 'ay', sep="")
    else:
        print(a[first:], a[:first], 'ay', sep="")