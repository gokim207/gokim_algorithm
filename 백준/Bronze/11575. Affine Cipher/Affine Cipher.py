al = [i for i in range(0, 26)]
for i in range(int(input())):
    a,b = map(int,input().split())
    x = input()
    for j in x:
        y = (a*al[ord(j)-65]+b)%26
        print(chr(y + 65),end="")
    print()