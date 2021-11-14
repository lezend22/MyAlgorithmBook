import sys
from collections import deque

r, c = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]

chez = []


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs():
    visited = [[0] * c for _ in range(r)]
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 1
    cnt = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                if arr[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                elif arr[nx][ny] == 1:
                    arr[nx][ny] = 0
                    cnt += 1
                    visited[nx][ny] = 1
    chez.append(cnt)
    return cnt


loopCount = 0
while True:

    count = dfs()
    if count == 0:
        break
    loopCount += 1
print(loopCount)
print(chez[-2])