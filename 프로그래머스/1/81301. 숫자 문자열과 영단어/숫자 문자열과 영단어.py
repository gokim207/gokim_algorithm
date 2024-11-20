def solution(s):
    answer = ''
    num = {'zero':0, 'one' : 1, 'two' : 2, 'three': 3, 'four' : 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    x = ''
    for i in s:
        try:
            i = int(i)
            answer += str(i)
            x = ''
            continue
        except:
            x += i
        
        if x in num:
            answer += str(num[x])
            x = ''
    return int(answer)