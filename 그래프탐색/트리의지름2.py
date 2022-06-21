import heapq
import sys

nonleaf = set()
INF = 1e9
max_ = 0
n = int(sys.stdin.readline())
leaf = set([x for x in range(1, n+1)])
arr = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b, c = map(int, sys.stdin.readline().split())
    nonleaf.add(a)
    arr[a].append((b, c))
    arr[b].append((a, c))

leaf = leaf - nonleaf
print(leaf)

def dijkstra(start):
    global max_
    distance = [INF] * (n+1)
    visited = [False] * (n+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now, = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in arr[now]:
            if not visited[i[0]]:
                visited[i[0]] = True
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

    print("##", start, distance)

    tmp = []
    for k in leaf:
        tmp.append(distance[k])
    tmp.sort()
    print(tmp[-1], tmp[-2])
    max_ = max(max_, tmp[-1] + tmp[-2])

for i in nonleaf:
    dijkstra(i)

print(max_)