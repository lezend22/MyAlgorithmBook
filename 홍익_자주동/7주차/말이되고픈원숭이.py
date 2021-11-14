import sys
from collections import deque

k = int(sys.stdin.readline())
w, h = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]

dx1 = [-1, 0, 1, 0]
dy1 = [0, -1, 0, 1]
dx2 = [-1, -2, -2, -1, 1, 2, 2, 1]
dy2 = [-2, -1, 1, 2, 2, 1, -1, -2]


def bfs():
    queue = deque()
    queue.append((0, 0, k))
    visited = [[[0 for i in range(31)] for i in range(w)] for i in range(h)]
    while queue:
        x, y, z = queue.popleft()

        if x == h-1 and y == w-1:
            #return count
            return visited[x][y][z]

        for i in range(4):
            nx = x + dx1[i]
            ny = y + dy1[i]
            if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] != 1 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                queue.append((nx, ny, z))

        if z > 0:
            for i in range(8):
                nx = x + dx2[i]
                ny = y + dy2[i]
                if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] != 1 and visited[nx][ny][z-1] == 0:
                    visited[nx][ny][z-1] = visited[nx][ny][z] + 1
                    queue.append((nx, ny, z-1))

    return -1

print(bfs())