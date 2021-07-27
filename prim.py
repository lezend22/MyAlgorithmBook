import sys

# prim알고리즘
# 노드의 개수 N, Weight 가중치그래프 입력
# MST 출력

INF = sys.maxsize
N = int(sys.stdin.readline())
W = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(W)
nearest = [0 for i in range(N)]
vnear = 0
F = []
print(nearest)

distance = []
for i in range(N):
    distance.append(W[i][0])

print(distance)

node = 0
while node < N - 1:

    minimum = INF
    for i in range(1, N):
        if 0 <= distance[i] <= minimum:
            minimum = distance[i]
            vnear = i

    print(vnear)

    #출력시 보기좋게 하기위해 1씩더해놓음
    e = [nearest[vnear]+1, vnear+1]
    F.append(e)
    distance[vnear] = -1

    for i in range(1, N):
        if W[i][vnear] < distance[i]:
            distance[i] = W[i][vnear]
            nearest[i] = vnear
    node += 1

print(F)