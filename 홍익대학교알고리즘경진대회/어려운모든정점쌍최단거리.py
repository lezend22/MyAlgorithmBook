import sys
from collections import deque

n,m,k = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

p1 = 0
for i in range(1, m+1):
    a, b = map(int, sys.stdin.readline().split())
    if i == k:
        p1 = a
        continue
    graph[a].append(b)
    graph[b].append(a)

vx = [0] * (n+1)

queue = deque()
queue.append(p1)
vx[p1] = 1
while queue:
    popleft = queue.popleft()
    for v in graph[popleft]:
        if vx[v]:
            continue
        vx[v] = 1
        queue.append(v)


print(sum(vx)*(n-sum(vx)))



