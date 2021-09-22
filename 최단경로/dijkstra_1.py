### 가독성, 직관성 so bad,,
import sys

INF = int(1e9)

n,m = map(int, sys.stdin.readline().split())
start = int(input())
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))

def getSmallestNode():
    minValue = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < minValue and not visited[i]:
            minValue = distance[i]
            index = i
    return index

def dijkstra(start):

    distance[start] = 0
    visited[start] = True
    # start 시작노드에 대해서 초기화
    for j in graph[start]:

        distance[j[0]] = j[1]

    #시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문처리
        now = getSmallestNode()
        visited[now] = True

        #현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]

            if cost<distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1):

    if distance[i] == INF:
        print("can't reach")
    else:
        print(distance[i])
