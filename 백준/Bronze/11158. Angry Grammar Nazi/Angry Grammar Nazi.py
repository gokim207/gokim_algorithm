d = ['u', 'ur']
for i in range(int(input())):
    x = input().split()
    result = 0
    for j in range(len(x)):
        if x[j] in d:
            result += 1
            continue
        try:
            if (x[j] == 'should' or x[j] == 'would') and len(x)-1 != j:
                if x[j+1] == 'of':
                    result += 1
        except:
            result = result
        
        a = x[j].find("lol")
        if a != -1:
            result += 1
    print(result*10)