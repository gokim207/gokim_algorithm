n = int(input())
a = input()
length = 0
result = ''

for i in a:
    if i == 'J' or i == 'A' or i == 'V':
        length += 1
    else:
        result += i
if length == n:
    print('nojava')
    exit()
else:
    print(result)