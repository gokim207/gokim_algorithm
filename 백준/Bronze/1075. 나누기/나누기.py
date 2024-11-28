n = input()
a = int(input())

for i in range(0, 100):
    if i < 10:
        i = '0' + str(i)
    else:
        i = str(i)
    new_n = n[:-2] + i
    if int(new_n) % a == 0:
        print(i)
        exit()
        
