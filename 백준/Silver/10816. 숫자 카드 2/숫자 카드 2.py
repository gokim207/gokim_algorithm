import sys
a = sys.stdin.readline()
b = list(sys.stdin.readline().rstrip().split())
c = sys.stdin.readline()
d = list(sys.stdin.readline().rstrip().split())
e={}

for i in b:
   if(i in e):
       e[i]+=1 
   else:
       e[i]=1
       
for i in d:
    if(i in e):
        print(e[i],end=" ")
    else:
        print('0',end=" ")