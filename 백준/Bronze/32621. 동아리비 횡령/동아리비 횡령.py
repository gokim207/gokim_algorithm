n = input()

if n.find('+') == -1:
    print('No Money')
    exit()
x = n[:n.find('+')]
y = n[n.find('+')+1:]
if x == '' or y == '':
    print('No Money')
    exit()
if x != y or x[0] == '0' or y[0] == '0':
    print('No Money')
    exit()
    
for i in range(len(x)):
    if not x[i].isdigit() or not y[i].isdigit():
        print('No Money')
        exit()
print('CUTE')