while True:
    x = int(input())
    if x == 0:
        break
    result = 0
    for i in range(1, x+1):
        result += i**2
    print(result)