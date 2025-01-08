single = ['Yakk', 'Doh', 'Seh', 'Ghar', 'Bang', 'Sheesh']
double = ["Habb Yakk","Dobara","Dousa","Dorgy","Dabash","Dosh"]
for i in range(int(input())):
    x,y = map(int,input().split())
    if x == y:
        print(f"Case {i+1}: {double[x-1]}")
    else:
        if (x == 6 and y == 5) or (x == 5 and y == 6):
            print(f'Case {i+1}: Sheesh Beesh')
        else:
            print(f"Case {i+1}: {single[max(x-1,y-1)]} {single[min(x-1,y-1)]}")