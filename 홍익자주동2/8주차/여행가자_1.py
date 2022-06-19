import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

# i번째줄 j번째 열이 이어져있으면 1인 형태의 graph 입력
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# travel하는 도시 num
travel = list(map(int, sys.stdin.readline().split()))
road = []

# 
def find(parent, target):
    if parent[target] != target:
        return find(parent, parent[target])
    return target

# 작은 노드가 부모가 되도록 함.
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 입력 받은 graph를 완탐하여 (i, j) 로 경로를 전부 저장함.
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            road.append((i+1, j+1))

# parent 부모 노드를 각자 자신으로 초기화, 이때 n+1로 주어 0인덱스 무시
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

# (i, j) 경로를 가져와 각 노드의 parent를 바꿔줌 (union으로)
for i in range(len(road)):
    a, b = road[i]
    union(parent, a, b)
#
# print(road)
# print(parent)
# print('각 원소가 속한 집합: ', end='')
# for i in range(ssg, n + ssg):
#     print(find(parent, i), end=' ')
#
# print('부모 테이블: ', end='')
# for i in range(ssg, n + ssg):
#     print(parent[i], end=' ')

result = []
for i in range(len(travel)):
    if not result:
        result.append(find(parent, travel[i]))

    else:
        if find(parent, travel[i]) not in result:
            print("NO")
            exit(0)
        else:
            continue
print("YES")

