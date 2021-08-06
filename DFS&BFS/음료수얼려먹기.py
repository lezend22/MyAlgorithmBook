import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
print(arr)

queue = deque()
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
direct = [0, 1, 2, 3]
visited = list()
count = 0

def findIce():
    while True:
        if queue:
            i, j = queue.popleft()
            visited.append((i,j))
            for d in direct:
                nx = i + dx[d]
                ny = j + dy[d]
                if nx >= 0 and nx < n and ny >= 0 and ny < m:
                    if arr[nx][ny] == 0 and (nx,ny) not in visited:
                        queue.append((nx,ny))
        else:
            global count
            count += 1
            break




##start
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0 and (i,j) not in visited:
            queue.append((i,j))
            findIce()

print(count)