n = int(input())
a = list(input().split())
b = list(input().split()) 
x = ''
y = ''
for i in a:
    x += i
for i in b:
    y += i
if int(x) < int(y):
    print(x)
else:
    print(y)