import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
captain = [1e9] * (n+1)

while True:
    a, b = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1:
        break
    graph[a].append(b)
    graph[b].append(a)

def bfs(k):

    visited = []
    queue = deque()
    cnt = 0
    queue.append((k, cnt))
    visited.append(k)

    while queue:
        nd, cnt = queue.popleft()
        if len(visited) == n:
            captain[k] = cnt
        for node in graph[nd]:
            if node not in visited:
                queue.append((node, cnt+1))
                visited.append(node)


for i in range(1, n+1):
    bfs(i)


capNum = min(captain)
posIndex = [x for x in range(1, len(captain)) if captain[x] == capNum]

# 노드 n이 1개일때 예외처리
if capNum == 0:
    capNum = 1
print(capNum, len(posIndex))
for i in posIndex:
    print(i, end=" ")