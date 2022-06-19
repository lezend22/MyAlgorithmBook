import sys

N = int(sys.stdin.readline())

graph = [(1, 2, 32), (1, 4, 17), (2, 5, 45), (3, 4, 18), (4, 5, 10), (5, 6, 28), (3, 7, 5), (4, 8, 3), (5, 9, 25),
         (6, 10, 6), (7, 8, 59), (8, 9, 4), (9, 10, 12)]
#graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(graph)
graph.sort(key=lambda x:x[2]) #가중치로 간선 정렬 format = (정점1, 정점2, 가중치)
print(graph)

# MST, P 각 정점의 부분집합 선언
F = []  # MST
p = [0]  # parent root

# could be Initialize
for i in range(1, N + 1):
    p.append(i)  # 각 정점이 집합의 대표

print(p)

def find(u):
    if u != p[u]:
        p[u] = find(p[u])
    return p[u]


def union(u, v):
    root1 = find(u)
    root2 = find(v)
    p[root2] = root1


tree_edge = 0
F_cost = 0

while True:
    if tree_edge == N - 1:
        break
    u, v, wt = graph.pop(0)
    print(u, v, wt)
    if find(u) != find(v):
        union(u, v)
        F.append((u, v))
        F_cost += wt
        tree_edge += 1
        print(p)

print("MST = ", F)

print("MST Cost = ", F_cost)
