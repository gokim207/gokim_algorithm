d = [chr(i) for i in range(65, 91)]
a = input()
for i in a:
    print(d[(ord(i)-68)],end="")