from datetime import datetime
d,m = input().split()
date = f'2009-{m}-{d}'
date_time = datetime.strptime(date, '%Y-%m-%d')
datelist = {1 : 'Monday', 2 : "Tuesday", 3 : "Wednesday", 4: "Thursday", 5:"Friday", 6 : "Saturday", 7 : "Sunday"}
print(datelist[date_time.weekday()+1])
