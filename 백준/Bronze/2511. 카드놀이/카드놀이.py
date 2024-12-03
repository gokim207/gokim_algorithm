a = list(map(int,input().split()))
b = list(map(int,input().split()))
a_score = 0
b_score = 0
winner = 'D'
for i in range(len(a)):
    if a[i] > b[i]:
        a_score += 3
        winner = 'A'
    elif a[i] < b[i]:
        b_score += 3
        winner = 'B'
    else:
        a_score += 1
        b_score += 1
print(a_score, b_score)
if a_score > b_score:
    print('A')
elif a_score < b_score:
    print('B')
else:
    if winner != 'D':
        print(winner)
    else:
        print('D')