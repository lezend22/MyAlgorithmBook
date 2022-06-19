#
# def dfs(curr):
#     global discover
#     global visited
#     global answer
#     if curr not in discover:
#         discover.add(curr)
#         visited.append(curr)
#         for next in graph[curr]:
#             if next not in visited:
#                 dfs(next)
#     else:
#         answer = False

import sys

n = int(sys.stdin.readline())
edge = []
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    edge.append((a, b))
    graph[a].append(b)
    graph[b].append(a)

cut = {0}
for i in range(1, n+1):
    if len(graph[i]) > 1:
        cut.add(i)

q = int(sys.stdin.readline())
for _ in range(q):
    t, k = map(int, sys.stdin.readline().split())
    # 단절점구하기
    if t == 1:
        # 간선이 2개이상
        if k in cut:
            print("yes")
        else:
            print("no")

    # 단절선 구하기
    elif t == 2:
        if n == 2:
            print("yes")
            continue
        a, b = edge[k-1]
        if a in cut or b in cut:
            print("yes")
        else:
            print("no")


