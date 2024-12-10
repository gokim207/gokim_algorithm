import fractions
import math
import sys
input = sys.stdin.readline
g = 0
l = 1
for i in range(int(input())):
    x,y = map(int,input().split())
    g = math.gcd(g, fractions.Fraction(x,y).numerator)
    l = math.lcm(l, fractions.Fraction(x,y).denominator)
print(g, l)