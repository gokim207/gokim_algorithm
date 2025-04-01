n = int(input())
card = list(map(int,input().split()))
print(sum(card) - max(card))