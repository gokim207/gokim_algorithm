a = 0
while 1:
    x = input()
    if x == '고무오리 디버깅 끝':
        break
    
    if x == '문제':
        a += 1
    elif x == '고무오리':
        if a == 0:
            a += 2
        else:
            a -= 1
    
if a == 0:
    print('고무오리야 사랑해')
else:
    print('힝구')