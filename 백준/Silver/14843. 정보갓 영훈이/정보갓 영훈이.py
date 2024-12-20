n = int(input())
score = 0
for i in range(n):
    s,a,t,m = map(float, input().split())
    score += (s*(1+1/a)*(1+m/t))/4

rank  = 1
m = int(input())
for i in range(m):
    x = float(input())
    if x > score:
        rank += 1

if (m+1)*0.15 >= rank:
    print(f'The total score of Younghoon "The God" is {score:.2f}.')
else:
    print(f'The total score of Younghoon is {score:.2f}.')