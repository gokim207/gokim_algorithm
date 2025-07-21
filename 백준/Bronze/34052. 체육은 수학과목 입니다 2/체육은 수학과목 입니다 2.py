a = []
for i in range(4):
    a.append(int(input()))
print('Yes' if sum(a)+300 <= 1800 else 'No')