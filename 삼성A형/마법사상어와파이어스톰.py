from collections import deque

n, q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(pow(2, n))]
magic = list(map(int, input().split()))
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def rotate(a, b, g):
    temp = {}
    x, y = a, b
    for i in range(b, b+g):
        y = b
        for j in range(a+g-1, a-1, -1):
            temp[(x, y)] = arr[j][i]
            y += 1
        x += 1

    return temp

def reduce():
    temp = [[0] * length for _ in range(length)]
    for x in range(length):
        for y in range(length):
            if arr[x][y] != 0:
                iceCnt = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < length and 0 <= ny < length and arr[nx][ny] > 0:
                        iceCnt += 1
                if iceCnt < 3:
                    temp[x][y] -= 1

    for i in range(length):
        for j in range(length):
            arr[i][j] = arr[i][j] + temp[i][j]

def findLarge(a, b):
    global visited
    queue = deque()
    queue.append((a, b))
    visited[a][b] = True
    maxCnt = 1
    while queue:

        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < length and 0 <= ny < length and arr[nx][ny] > 0 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                maxCnt += 1

    return maxCnt

def findPiece():
    iceSum = 0
    secAns = 0
    for i in range(length):
        for j in range(length):
            if arr[i][j] != 0:
                iceSum += arr[i][j]
                if not visited[i][j]:
                    secAns = max(secAns, findLarge(i, j))
    return iceSum, secAns

def show():
    for i in arr:
        print(i)
    print("#########")


length = pow(2, n)
for l in magic:
    g = pow(2, l)
    # show()
    for sx in range(0, length, g):
        for sy in range(0, length, g):
            t = rotate(sx, sy, g)
            for key, val in t.items():
                x, y = key
                arr[x][y] = val
    # show()
    reduce()
    visited = [[False] * length for _ in range(length)]

a1, a2 = findPiece()
print(a1)
print(a2)