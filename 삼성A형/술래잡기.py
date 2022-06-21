n, m, h, k = map(int, input().split())
arr = [[[] for _ in range(n)] for _ in range(n)]
tree = []
cx, cy = n // 2, n // 2
answer = 0
for i in range(m):
    x, y, d = map(int, input().split())
    # 도망자 1
    arr[x - 1][y - 1].append((d))
for i in range(h):
    x, y = map(int, input().split())
    tree.append((x - 1, y - 1))


def move(x, y, dir):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    nx = x + dx[dir]
    ny = y + dy[dir]
    if 0 <= nx < n and 0 <= ny < n:
        if cx == nx and cy == ny:
            return x, y, dir
        return nx, ny, dir
    else:
        dir = (dir + 2) % 4
        nx = x + dx[dir]
        ny = y + dy[dir]
        if nx == cx and ny == cy:
            return x, y, dir
        return nx, ny, dir


def runnerMove():
    global cx, cy
    temp = [[[] for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if not arr[i][j]:
                continue
            for k in arr[i][j]:
                dist = abs(cx - i) + abs(cy - j)
                if dist <= 3:
                    nx, ny, d = move(i, j, k)
                    temp[nx][ny].append(d)
                else:
                    temp[i][j].append(k)
    return temp


def catcherMove(count, movement):
    global answer, cx, cy
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    idx = count % movement
    nx, ny, d = path[idx]
    # print(count, ':', nx, ny)
    cx, cy = nx, ny
    d = d % 4
    # print(nx, ny, d)
    for i in range(3):
        nnx = nx + dx[d] * i
        nny = ny + dy[d] * i
        if 0 <= nnx < n and 0 <= nny < n and arr[nnx][nny] and (nnx, nny) not in tree:
            answer += (count * len(arr[nnx][nny]))
            arr[nnx][nny] = []


def getPath():
    path = [(n // 2, n // 2, 0)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    sx, sy = n // 2, n // 2
    dir, cnt, mcnt, dcnt = 0, 0, 1, 1

    while not (sx == 0 and sy == 0):
        cnt += 1
        sx = sx + dx[dir]
        sy = sy + dy[dir]
        if mcnt == cnt:
            cnt = 0
            dir += 1
            if dcnt == 2:
                dcnt = 0
                mcnt += 1
            dcnt += 1
        dir = dir % 4
        path.append((sx, sy, dir))

    # 0 위 / 1 오른쪽 / 2 아래 / 3 왼쪽
    path2 = []
    sx, sy = 0, 0
    dir, cnt, mcnt, dcnt = 2, 0, n - 1, 0
    while not (sx == (n // 2) and sy == (n // 2)):
        cnt += 1
        sx = sx + dx[dir]
        sy = sy + dy[dir]
        if mcnt == cnt:
            cnt = 0
            dir -= 1
            if dcnt == 2:
                dcnt = 0
                mcnt -= 1
            dcnt += 1
        if dir < 0:
            dir = 4 + dir
        # print(sx, sy, mcnt)
        path2.append((sx, sy, dir))

    # print(len(path), path)
    path.pop()
    path.append((0, 0, 2))

    path2.pop()
    # print(len(path2), path2)
    path += path2
    return path, len(path)


def show():
    for i in arr:
        print(i)
    print("##########")


path, movement = getPath()
count = 1
while count <= k:
    # print("init")
    # show()
    arr = runnerMove()
    # print("runner")
    # show()
    catcherMove(count, movement)
    # print('catch')
    # show()
    count += 1

print(answer)
