a = input()
result = 0
lenght = 0

for i in a:
    if i == '+':
        result += 0.5
        continue
    else:
        if i == 'A':
            result += 4
        elif i == 'B':
            result += 3
        elif  i == 'C':
            result += 2
        elif i == 'D':
            result += 1
        lenght += 1
print(result / lenght)