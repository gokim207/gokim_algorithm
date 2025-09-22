import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = sorted(set(a))

d = {v: i for i, v in enumerate(b)}
print(' '.join(str(d[v]) for v in a))