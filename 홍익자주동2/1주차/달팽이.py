import sys

n = int(sys.stdin.readline())
a = int(sys.stdin.readline())

arr = [[0] * n for _ in range(n)]
visited = [[0] * n for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

mid = n // 2
x, y = 0, 0
i = 1
m = n*n
val = [0] * (m+1)
arr[x][y] = m
val[m] = (x, y)
visited[x][y] = 1
m -= 1

while True:

    if m == 1:
        arr[mid][mid] = 1
        val[m] = (mid, mid)
        break

    k = i % 4
    nx = x + dx[k]
    ny = y + dy[k]

    if 0<= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
        arr[nx][ny] = m
        val[m] = (nx, ny)
        visited[nx][ny] = 1
        x, y = nx, ny
        m -= 1

    else:
        i += 1

for i in arr:
    for j in range(n):
        if j == n-1:
            print(i[j])
        else:
            print(i[j], end=' ')

x, y = val[a]
print(x+1, y+1)