import sys
sys.setrecursionlimit(10000)
INF = 1e9
n = int(sys.stdin.readline())
arr = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, sys.stdin.readline().split())
    arr[a].append((b, c))
    arr[b].append((a, c))

distance = [INF] * (n+1)
distance[1] = 0
visited = []

def dfs(s, w):
    for i in arr[s]:
        cost = w + i[1]
        if distance[i[0]] > cost:
            distance[i[0]] = cost
            visited.append(i[0])
            dfs(i[0], cost)

# 루트에서 가장 먼 리프 찾기
dfs(1, 0)
distance = distance[1:]
index = distance.index(max(distance))

# 리프에서 가장 먼 다른 리프 찾기
distance = [INF] * (n+1)
distance[index+1] = 0
visited = []
dfs(index+1, 0)

ans2 = max(distance[1:])
print(ans2)
