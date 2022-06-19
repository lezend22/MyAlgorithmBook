import sys
sys.setrecursionlimit(500000)

n,m,k = map(int,sys.stdin.readline().split())
graph = [i for i in range(n+1)] #각 노드의 부모를 자기 자신으로 초기화

def parent_find(x):
    if graph[x] != x:
        graph[x] = parent_find(graph[x])
    return graph[x]

def union_find(x, y):
    x = parent_find(x)
    y = parent_find(y)
    if x != y: #서로 루트노드가 다르면
        graph[x] = y #연결함 x의 부모는 y
                    #따로 크기에 따라서 정렬 안했으므로 x의부모는 y로 모두 넣어짐

p1 = 0
for i in range(1, m+1):
    a, b = map(int, sys.stdin.readline().split())
    if i == k:
        if a == b:
            print(0)
            exit(0)
        p1 = (a, b)
    else:
        union_find(a, b)

for i in range(1, n+1):
    parent_find(i)

aCount = 0
bCount = 0
for i in range(1, n+1):

    if graph[i] == graph[p1[0]]:
        aCount += 1
    # elif graph[i] == graph[p1[ssg]]:
    #     bCount += ssg

print(aCount * (n-aCount))




