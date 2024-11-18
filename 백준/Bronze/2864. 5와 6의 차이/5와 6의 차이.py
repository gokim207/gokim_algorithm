a,b = input().split()
result = []
new_a, new_b = '', ''
for i in a:
    if i == '6':
        new_a += '5'
    else:
        new_a += i
for i in b:
    if i  == '6':
        new_b += '5'
    else:
        new_b += i
result.append(int(new_a) + int(new_b))
new_a, new_b = '', ''
for i in a:
    if i == '5':
        new_a += '6'
    else:
        new_a += i
for i in b:
    if i  == '5':
        new_b += '6'
    else:
        new_b += i
result.append(int(new_a) + int(new_b))

print(*result)