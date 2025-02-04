a,b = map(int,input().split())
n = int(input())
find = []

for i in range(n):
    c = int(input())
    if c == b:
        print(1)
        exit()
    find.append(abs(b-c))
    
print(min(min(find)+1, abs(a-b)))