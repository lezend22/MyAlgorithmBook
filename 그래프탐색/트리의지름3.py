import heapq
import sys

INF = 1e9
max_ = 0
n = int(sys.stdin.readline())
arr = [[] for _ in range(n+1)]
node = set([x for x in range(1, n+1)])
nonleaf = set()
for i in range(n-1):
    a, b, c = map(int, sys.stdin.readline().split())
    nonleaf.add(a)
    arr[a].append((b, c))
    arr[b].append((a, c))

leaf = node - nonleaf

def dijkstra(start):
    global visited, max_
    distance = [INF] * (n+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now, = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for k in arr[now]:
            cost = dist + k[1]
            if distance[k[0]] > cost:
                distance[k[0]] = cost
                heapq.heappush(q, (cost, k[0]))

    m_ = 0
    for m in range(1, n+1):
        if distance[m] != INF and m in leaf:
            m_ = max(m_, distance[m])

    max_ = max(max_, m_)

visited = []
for i in leaf:
    dijkstra(i)
    visited.append(i)

print(max_)
