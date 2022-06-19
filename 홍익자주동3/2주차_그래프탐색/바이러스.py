import sys
from collections import deque

n = int(sys.stdin.readline())
edge = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for _ in range(edge):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
visited = set()
queue.append(1)
visited.add(1)

while queue:
    
    popleft = queue.popleft()

    for node in graph[popleft]:
        if node not in visited:
            queue.append(node)
            visited.add(node)

# print(visited)
print(len(visited)-1)