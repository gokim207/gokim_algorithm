hour = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", 'ten', "eleven", "twelve"]
minute = ["o' clock", "one minute", "two minutes", "three minutes", "four minutes", "five minutes", "six minutes", "seven minutes", "eight minutes", "nine minutes", "ten minutes", "eleven minutes", "twelve minutes", "thirteen minutes", "fourteen minutes", "quarter", "sixteen minutes", "seventeen minutes", "eighteen minutes", "nineteen minutes", "twenty minutes", "twenty one minutes", "twenty two minutes", "twenty three minutes", "twenty four minutes", "twenty five minutes", "twenty six minutes", "twenty seven minutes", "twenty eight minutes", "twenty nine minutes"]
a = int(input())
b = int(input())

if b > 30:
    b = 60 - b
    a = (a+1)%12
    print(minute[b], 'to', hour[a-1])
else:
    if b == 0:
        print(hour[a-1], minute[b])
    elif b == 30:
        print('half past', hour[a-1])
    else:
        print(minute[b], 'past', hour[a-1])