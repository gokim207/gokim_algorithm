n = int(input())
a = list(input().split())
b = list(input().split())
for i in a:
    if i not in b:
        print(i)
        exit()