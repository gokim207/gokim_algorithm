n = int(input())
a = input()

for i in range(n-1):
    if a[2*i + 1] == a[2*i + 2]:
        print("No")
        exit()
                
print("Yes")