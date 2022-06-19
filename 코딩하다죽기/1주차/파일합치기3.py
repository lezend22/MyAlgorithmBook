import heapq
import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))

    heapq.heapify(arr)
    total = []
    while len(arr) != 1:
        a = heapq.heappop(arr)
        b = heapq.heappop(arr)
        tmp = a + b
        total.append(tmp)
        heapq.heappush(arr, tmp)

    print(sum(total))
