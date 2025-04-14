import sys
sys.setrecursionlimit(10**6)

arr={1:1,2:1, 3:1, 4:2, 5:2, 6:3, 7:4}
def pado(n):
   if n in arr:
      return arr[n]
   arr[n] = pado(n-2)+pado(n-3)
   return arr[n]


for i in range(int(input())):
    x = int(input())
    print(pado(x))