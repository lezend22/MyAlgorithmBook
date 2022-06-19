import sys
from collections import deque

n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

edge = [1e9] * (n+1)
edge[x] = 0

queue = deque()
visited = set()
cnt = 0
queue.append((x, cnt))


while queue:

    node, cnt = queue.popleft()
    # print(node, cnt)
    cnt += 1
    if cnt > k and queue:
        continue

    for nd in graph[node]:
        if edge[nd] < cnt:
            continue
        else:
            edge[nd] = cnt
            queue.append((nd, cnt))
    # print(queue)
# print(edge)
flag = False
for i in range(1, len(edge)):
    if edge[i] == k:
        flag = True
        print(i)

if not flag:
    print(-1)