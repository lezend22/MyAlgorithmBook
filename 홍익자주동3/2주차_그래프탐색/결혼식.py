import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for _ in range(m):

    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
visited = set()
cnt = 0
queue.append((1, cnt))
visited.add(1)

while queue:

    nd, cnt = queue.popleft()
    # print(nd, cnt)
    for node in graph[nd]:
        if node not in visited and cnt < 2:
            visited.add(node)
            queue.append((node, cnt+1))

# print(visited)
print(len(visited)-1)
