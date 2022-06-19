from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def bfs(loc, color):

    queue = deque()
    queue.append(loc)
    path = [loc]
    rainbow = 0
    rainbows = []
    while queue:
        x, y, = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and (arr[nx][ny] == color or arr[nx][ny] == 0) and not totalVisit[nx][ny]:
                if arr[nx][ny] == 0:
                    rainbow += 1
                    rainbows.append((nx, ny))
                totalVisit[nx][ny] = True
                queue.append((nx, ny))
                path.append((nx, ny))

    for a, b in rainbows:
        totalVisit[a][b] = False

    return [len(path), rainbow, path]

def findBlock():
    blocks = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0:
                totalVisit[i][j] = True
                pivot = arr[i][j]
                pos = bfs((i, j), pivot)
                if pos[0] >= 2:
                    blocks.append(pos)
    blocks.sort(reverse=True)
    return blocks

def getDown(loc):
    x, y = loc
    val = arr[x][y]
    nx = x + 1
    while True:
        if nx >= n:
            break
        if arr[nx][y] != -5:
            break

        nx = nx + 1

    arr[x][y] = -5
    arr[nx - 1][y] = val


def gravity():
    for i in range(n - 2, -1, -1):  # 밑에서 부터 체크
        for j in range(n):
            if arr[i][j] > -1:  # -1이 아니면 아래로 다운
                r = i
                while True:
                    if 0 <= r + 1 < n and arr[r + 1][j] == -5:  # 다음행이 인덱스 범위 안이면서 -2이면 아래로 다운
                        arr[r + 1][j] = arr[r][j]
                        arr[r][j] = -5
                        r += 1
                    else:
                        break

def rotate():
    temp = [[0] * n for _ in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(n):
            temp[n-1-i][j] = arr[j][i]

    return temp

def show():
    print("###########")
    for i in arr:
        print(i)

answer = 0
while True:
    totalVisit = [[False] * n for _ in range(n)]
    block = findBlock()
    if len(block) == 0:
        break

    b = block[0][0]
    for x, y in block[0][2]:
        arr[x][y] = -5

    # show()
    answer += (b*b)
    # print(answer, b*b)
    gravity()
    # show()
    arr = rotate()
    # show()
    gravity()
    # show()

print(answer)

