import sys
from collections import deque

def dfs(i, j, visited):
    global life
    pivot = graph[i][j]
    queue = deque()
    queue.append((i, j))
    temp = [(i, j)]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in temp and graph[nx][ny] == pivot:
                queue.append((nx, ny))
                temp.append((nx, ny))
    #여기까지 퍼지는 칸 구함 temp이 퍼져있는 결과 칸
    # print(temp)
    flag = False
    pk = -1
    for k in range(len(temp)):
        a, b = temp[k]
        if not flag and graph[a][b] != result[a][b]:
            # print(graph[a][b], result[a][b])
            flag = True
            pk = result[a][b]
            life -= 1

            # temp에서 k번째 까지 이미 확인한 result 블록중 변한 값과 다른 값이 있는지 확인
            for t in range(k):
                a1, b1 = temp[t]
                if result[a1][b1] != pk:
                    print("NO")
                    exit(0)

        if flag:
            if result[a][b] != pk:
                # print(pk, result[a][b])
                print("NO")
                exit(0)
            else:
                continue

    visited += temp

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    result = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    visited = []
    life = 1
    for i in range(n):
        for j in range(m):
            if (i, j) not in visited:
                dfs(i, j, visited)
            if life < 0:
                print("NO")
                exit(0)
    print("YES")
