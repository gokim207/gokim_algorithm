s = input()
if '0x' in s:
    print(int(s, 16))
elif s[0] == '0':
    print(int(s, 8))
else:
    print(int(s))