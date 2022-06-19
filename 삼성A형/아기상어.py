from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
check = [[False] * n for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def checkFish():
    cnt = 0
    for i in range(n):
        for j in range(n):
            if 9 > arr[i][j] > 0:
                cnt += 1
    return cnt

def addNum():
    global sx, sy
    ret = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0 and arr[i][j] != 9:
                if arr[i][j] < shark:
                    ret += abs(sx - i) + abs(sy - j)
    return ret

def findNearestQueue(x, y):
    path = []
    queue = deque()
    queue.append((x, y, 0))
    visited = {(x, y)}
    minDist = 1e9
    while queue:

        x, y, dist = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] <= shark and (nx, ny) not in visited:
                visited.add((nx, ny))
                if 0 < arr[nx][ny] < shark:
                    minDist = dist
                    path.append((dist+1, nx, ny))
                if dist+1 <= minDist:
                    queue.append((nx, ny, dist+1))

    return path

def eatFish(posLoc):
    global sx, sy, stamina, answer, shark
    dist, x, y = posLoc[0]
    answer += dist
    stamina += 1
    arr[x][y] = 9
    arr[sx][sy] = 0
    sx, sy = x, y

    if stamina == shark:
        shark += 1
        stamina = 0

def show():
    for i in arr:
        print(i)
    print(answer, shark)
    print("########")


sx, sy = -1, -1
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            sx, sy = i, j

answer = 0
shark = 2
stamina = 0
while True:
    t = checkFish()
    minCnt = 1e9

    path = findNearestQueue(sx, sy)
    if path:
        path.sort()
        eatFish(path)
    else:
        break

    # show()

print(answer)