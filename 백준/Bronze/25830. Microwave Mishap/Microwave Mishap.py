m, s = map(int, input().split(":"))
input_time = m * 60 + s
real_time = m * 3600 + s * 60

res = real_time - input_time

print(f"{res // 3600:0>2}:{res % 3600 // 60:0>2}:{res % 60:0>2}")