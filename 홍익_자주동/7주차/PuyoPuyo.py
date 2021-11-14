# 뿌요가 터질때, 터지고난후 내려올때
# 두가지로 분류
# popup이란 체크리스트를 둬서 popup이 4개면 터짐
# 후 down()으로 내려와
# down()구현이 진짜 너무 어려웠음, 항상 그림그려서 조건 차근차근따지자
import sys
from collections import deque

arr = [list(sys.stdin.readline().rstrip()) for _ in range(12)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(i, j, m):
    queue = deque()
    queue.append((i, j))
    popup.append((i, j))
    while queue:
        x, y = queue.popleft()
        for p in range(4):
            nx = x + dx[p]
            ny = y + dy[p]
            if 0 <= nx < 12 and 0 <= ny < 6 and not visited[nx][ny] and arr[nx][ny] == m:
                visited[nx][ny] = 1
                queue.append((nx, ny))
                popup.append((nx, ny))

def down():
    for i in range(6):
        for j in range(10, -1, -1):
            for k in range(11, j, -1):
                if arr[j][i] != '.' and arr[k][i] == ".":
                    arr[k][i] = arr[j][i]
                    arr[j][i] = '.'
                    break

count = 0
while True:
    flag = False
    visited = [[0] * 6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if arr[i][j] != '.' and not visited[i][j]:
                visited[i][j] = 1
                popup = []
                bfs(i, j, arr[i][j])
                if len(popup) == 4:
                    flag = True
                    for u in popup:
                        arr[u[0]][u[1]] = '.'
    if not flag:
        break
    down()
    count += 1
print(count)
