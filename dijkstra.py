import sys

### 수정해야함
INF = sys.maxsize

N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(graph)

v = [[0] * N]
distance = []

def getSmallIndex():
    minimum = INF
    for i in range(N):
        if distance[i] < minimum and v[i] is False:
            minimum = distance[i]
            index = i

    return index

def dijkstra(start):
    for i in range(N):
        distance.append(graph[start][i])

    v[start] = True
    for i in range(N - 2):
        current = getSmallIndex()
        v[current] = True
        for j in range(6):
            if v[j] is False:
                if distance[current] + graph[current][j] < distance[j]:
                    distance[j] = distance[current] + graph[current][j]


if __name__ == '__main__':
    dijkstra(0)
    for i in range(N):
        print(distance[i])
