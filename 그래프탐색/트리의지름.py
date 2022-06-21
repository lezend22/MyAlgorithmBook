import sys

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
    global visited
    for i in arr[s]:
        cost = w + i[1]
        if distance[i[0]] > cost:
            distance[i[0]] = cost
            visited.append(i[0])
            dfs(i[0], cost)

dfs(1, 0)
distance = distance[1:]
index = distance.index(max(distance))
index += 1
ans1 = max(distance)

visited = []
distance2 = [INF] * (n+1)
dfs(index, 0)

print(max(distance2) + ans1)