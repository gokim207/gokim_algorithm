one = ['A', 'a', 'b','D', 'd', 'e', 'g', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', '@']

n = input()
total = 0

for i in n:
    if i in one:
        total += 1
    elif i == 'B':
        total += 2
print(total)