n = int(input())
java = ['J', 'A', 'V']
a = input()
length = 0
result = ''

for i in a:
    if i in java:
        length += 1
    else:
        result += i
if length == n:
    print('nojava')
    exit()
else:
    print(result)

