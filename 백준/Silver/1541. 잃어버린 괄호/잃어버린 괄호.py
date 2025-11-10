a = input()
number = []
char = []
x = ""

def cal(a,b,c):
    if b == '+':
        return a + c
    else:
        return a - c

for i in a:
    if not i.isdigit():
        char.append(i)
        number.append(int(x))
        x = ""
    else:
        x += i
number.append(int(x))

result = 0
temp = ""
parts = a.split('-')

first = parts[0].split('+')
result = sum(map(int, first))

for part in parts[1:]:
    nums = part.split('+')
    result -= sum(map(int, nums))

print(result)