import heapq
n = int(input())
heap = []
result = 0

for i in range(n):
    heapq.heappush(heap, int(input()))
    
for i in range(n-1):
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    
    heapq.heappush(heap, a + b)
    result += a+b
print(result)