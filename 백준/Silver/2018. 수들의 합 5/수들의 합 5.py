n = int(input())
result = 0

def a(m):
	global n
	global result
	cnt = m
	
	# 받은 값이 n과 같으면
	if cnt == n:
		result += 1
		return
	
	# 받은 값이 n보다 크다면
	elif cnt > n:
		return
	i = 1
	
	# 작을 경우
	while 1:
		if cnt >= n:
			if cnt == n:
				result += 1
			break
		cnt += m+i
		i += 1
	

for i in range(1, n+1):
	a(i)
	
print(result)