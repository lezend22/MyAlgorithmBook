import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = []
total = []
maxC = 0

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[b].append(a)

def bfs(i):
    queue = deque()
    queue.append(i)
    v = [0 for _ in range(n+1)]
    v[i] = 1
    count = 1
    while queue:
        popleft = queue.popleft()
        for j in graph[popleft]:
            if not v[j]:
                v[j] = 1
                queue.append(j)
                count += 1

    return count

for i in range(1, len(graph)):
    if i not in visited and graph[i]:
        c = bfs(i)
        if c > maxC:
            maxC = c
        total.append((i, c))
for i in total:
    if i[1] == maxC:
        print(i[0], end=' ')


