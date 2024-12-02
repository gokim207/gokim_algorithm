a,b = map(int,input().split())
d = [chr(i) for i in range(97, 97+26)]
print('SN',a,end="")
result = ''

if b <= 26:
    print(d[b-1].upper())
    exit()
print(d[(b-1)//26-1], d[(b-1)%26],sep="")