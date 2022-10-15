import sys
from collections import defaultdict
sys.setrecursionlimit(100000)
MAX = 21

def dfs(start, d):

    depth[start] = d
    visited[start] = 1
    for node in graph[start]:
        if visited[node]:
            continue
        parent[node][0] = start
        dfs(node, d + 1)

def getDepth():

    for i in range(1, MAX):
        for j in range(1, n+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]

def lca(a, b):

    # b가 항상 깊음
    if depth[a] > depth[b]:
        a, b = b, a

    # 2^20 부터 2^0까지 depth 차이가 이보다 크면 b를 위로 끌어올림
    # 이후 2^0까지하므로 결국 a, b 의 depth 똑같아짐
    for i in range(MAX - 1, -1, -1):
        if depth[b] - depth[a] >= (1 << i):
            b = parent[b][i]

    # 바로 같으면 return
    if a == b:
        return a

    # 같이 위로 올라감. 똑같이 20위에 있는 것 부터 찾아봄.
    # 조상부터 1씩 내려옴. 만약 다르면 현재 i 만큼 올라감.
    # 이후 또 i 위에만큼이 다르면 계속 올라감.
    # 그러다 같은 순간이 옴. i = 0 마지막일때.
    for i in range(MAX - 1, -1, -1):
        # print(i, parent[a][i], parent[b][i])
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    # return 바로 위에꺼
    return parent[a][0]


n = int(sys.stdin.readline())
graph = defaultdict(list)
parent = [[0] * (MAX + 1) for _ in range(n + 1)]
depth = [0] * (n + 1)
visited = [0] * (n + 1)

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1, 0)
# print(depth)
getDepth()
# print(parent)

m = int(sys.stdin.readline())
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(lca(a, b))


