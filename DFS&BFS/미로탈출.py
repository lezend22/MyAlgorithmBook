import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]


queue = deque()
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
direct = [0, 1, 2, 3]
visited = list()

def findPath():
    count = 1
    while True:
        if not queue:
            print("no path")
            break

        i, j = queue.popleft()

        if (i, j) == (n-1, m-1):
            return arr[i][j]

        count = arr[i][j] + 1
        for d in direct:
            nx = i + dx[d]
            ny = j + dy[d]
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if arr[nx][ny] == 1 and (nx,ny) not in visited:
                    arr[nx][ny] = count
                    visited.append((nx,ny))
                    queue.append((nx, ny))


##start
i, j = 0, 0
queue.append((i,j))
print(findPath())

