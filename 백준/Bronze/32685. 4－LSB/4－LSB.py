a = bin(int(input()))[2:]
b = bin(int(input()))[2:]
c = bin(int(input()))[2:]
if len(a) >=5:
    a = a[-4:]
if len(b) >=5:
    b= b[-4:]
if len(c) >=5:
    c = c[-4:]

if len(a) <=3:
    while len(a) != 4:
        a = '0' + a
if len(b) <=3:
    while len(b) != 4:
        b = '0' + b
if len(c) <=3:
    while len(c) != 4:
        c = '0' + c
result = str(int(a + b + c, 2))
while len(result) < 4:
    result = '0' + result
print(result)