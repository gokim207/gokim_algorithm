n = int(input())
card = [i for i in range(1,n+1)]

for i in range(n-1):
    print(card[0],end=" ")
    new_card = card[2:]
    new_card.append(card[1])
    card = new_card
print(card[0])