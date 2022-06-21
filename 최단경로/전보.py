import heapq
import sys

INF = 1e9
n, m, c = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(n+1)]
for i in range(m):
    a, b, d = map(int, sys.stdin.readline().split())
    arr[a].append((b, d))


distance = [INF] * (n+1)
distance[c] = 0
q = []
heapq.heappush(q, (0, c))
while q:
    dist, now, = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for i in arr[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

cnt1 = 0
cnt2 = 0
for i in range(1, n+1):
    if distance[i] != INF:
        cnt1 += 1
        cnt2 = max(cnt2, distance[i])

# 동시에 전파되므로 제일 오래걸리는 것이 완료 시간
print(cnt1-1, cnt2)