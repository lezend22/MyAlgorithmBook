import heapq
import sys

n=int(sys.stdin.readline().strip())
heap = []

for _ in range(n):
    for a in map(int,sys.stdin.readline().split()):
        heapq.heappush(heap, a)

        if len(heap) == n+1:
            heapq.heappop(heap)

ans = heapq.heappop(heap)
print(ans)