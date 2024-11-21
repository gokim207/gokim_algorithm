a = input()
d = []

def cal(a):
    if(a=='(' or a==')'):
        return 0
    elif(a=='+' or a=='-'):
        return 1
    else:
        return 2

for i in a:
    if(i=='('):
        d.append('(')
    elif(i==')'):
        while 1:
            if(d[-1]=='('):
                d.pop(-1)
                break
            b = d.pop(-1)
            print(b,end="")
    elif(i in '+-*/'):
        while 1:
            if(len(d)==0):
                break
            if(cal(i) <= cal(d[-1])):
                b = d.pop(-1)
                print(b,end="")
            else:
                break
        d.append(i)
    else:
        print(i,end="")
        
d.reverse()
for i in d:
    print(i,end="")