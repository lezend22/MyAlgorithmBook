n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
moves = []
for i in range(m):
    tmp = list(map(int, input().split()))
    moves.append((tmp[0] - 1, tmp[1]))
cx = [0, -1, -1, -1, 0, 1, 1, 1]
cy = [-1, -1, 0, 1, 1, 1, 0, -1]

ex = [-1, -1, 1, 1]
ey = [-1, 1, 1, -1]


def moveCloud(cloud):
    d, s = move
    nCloud = []
    for c in cloud:
        px, py = c
        nx = (n + px + cx[d] * s) % n
        ny = (n + py + cy[d] * s) % n
        nCloud.append((nx, ny))
    # print(nCloud)
    return nCloud


def rain(nCloud):
    for c in nCloud:
        px, py = c

        arr[px][py] += 1
        visited[px][py] = True


def waterCopy(nCloud):
    for c in nCloud:
        x, y = c
        ccount = 0
        for i in range(4):
            nx = x + ex[i]
            ny = y + ey[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and arr[nx][ny] != 0:
                ccount += 1
        arr[x][y] += ccount


def reCloud(wasCloud):
    # print(wasCloud)

    for i in range(n):
        for j in range(n):

            if arr[i][j] >= 2 and visited[i][j] == False:
                arr[i][j] -= 2
                cloud.append((i, j))


cloud = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]
for cnt in range(m):
    move = moves[cnt]

    # print(arr)
    nCloud = moveCloud(cloud)
    # print(nCloud)
    visited = [[False] * n for _ in range(n)]
    rain(nCloud)

    # 초기화
    cloud = []
    # print(arr)
    waterCopy(nCloud)
    # print(arr)
    reCloud(nCloud)
    # print(newCloud)

    # print(arr)

# print(arr)
answer = 0
for i in range(n):
    answer += sum(arr[i])

print(answer)
