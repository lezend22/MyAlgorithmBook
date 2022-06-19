import heapq
import sys

n, c = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(n+1)]
m = int(sys.stdin.readline())
for i in range(m):
    a, b, d = map(int, sys.stdin.readline().split())
    heapq.heappush(arr[a], (b, d))

    # arr[a].append((b, d))


truck = []
cap = 0
ans = 0
for i in range(1, n+1):
    # print("######", i)
    # 빼기
    while truck:
        heappop = heapq.heappop(truck)
        if heappop[0] == i:
            # cap -= heappop[1]
            # print("out", heappop)
            ans += heappop[1]
        else:
            heapq.heappush(truck, heappop)
            break

    # 넣기
    next = []
    cap = 0

    for j in truck:
        heapq.heappush(arr[i], j)
    # for j in arr[i]:
    #     heapq.heappush(truck, j)
    while arr[i]:
        heapq_heappop = heapq.heappop(arr[i])

        cap += heapq_heappop[1]
        if cap > c:
            cap -= heapq_heappop[1]
            t = c - cap
            heapq.heappush(next, (heapq_heappop[0], t))
            break
        heapq.heappush(next, heapq_heappop)

    truck = next
    # print("truck", truck)

print(ans)
