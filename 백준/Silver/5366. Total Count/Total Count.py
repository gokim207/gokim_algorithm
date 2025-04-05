result = 0
d = {}
while 1:
    a = input()
    if a == '0':
        for k,v in d.items():
            print(k,v,sep= ": ")
        print(f'Grand Total: {result}')
        break
    
    if a not in d:
        d[a] = 1
    else:
        d[a] += 1
    result += 1