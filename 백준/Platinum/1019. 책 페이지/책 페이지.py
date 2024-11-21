import sys
input = sys.stdin.readline
d=[0]*10
n=int(input())
num = 1
def one_digit(number):  
    while number % 10 != 9:  
        for i in str(number):  
            d[int(i)] += num  
        number -= 1  

    return number  

while n>0:
    n = one_digit(n)  

    if n < 10:  
        for i in range(n+1):  
            d[i] += num  
    else:
        for j in range(10):  
            d[j] += (n//10 + 1) * num  

    d[0] -= num  
    num *= 10  
    n //= 10  
        
print(*d)