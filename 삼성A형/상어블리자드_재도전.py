
an, bn, cn = 0, 0, 0

def check(px, py):
    global an, bn, cn

    if arr[px][py] == 1:
        an += 1

    elif arr[px][py] == 2:
        bn += 1

    elif arr[px][py] == 3:
        cn += 1

def getPath():

    path = [(sx, sy)]
    mx = [0, 1, 0, -1]
    my = [-1, 0, 1, 0]
    nx, ny = sx, sy
    d, limit, change, cnt = 0, 1, 0, 0
    while True:

        nx, ny = nx + mx[d % 4], ny + my[d % 4]
        if not (0 <= nx < n and 0 <= ny < n):
            break

        path.append((nx, ny))
        cnt += 1

        if cnt == limit:
            change += 1
            d += 1
            cnt = 0
            if change == 2:
                change = 0
                limit += 1

    return path


def getMagic(d, s):

    # 1북, 2남, 3왼, 4오
    nx, ny = sx, sy
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(s):
        nx = nx + dx[d]
        ny = ny + dy[d]

        if 0 <= nx < n and 0 <= ny < n:
            # check(nx, ny)
            arr[nx][ny] = 0
        else:
            break


def moveBall():
    temp = []
    for p in range(1, len(path)):
        px, py = path[p]
        if arr[px][py]:
            temp.append(arr[px][py])

    i = 0
    for p in range(1, len(path)):
        px, py = path[p]
        if i < len(temp):
            arr[px][py] = temp[i]
            i += 1
        else:
            arr[px][py] = 0


def getBlow():
    blowFlag = False
    px, py = path[1]
    pivot = arr[px][py]
    temp = [(px, py)]

    for i in range(2, len(path)):
        px, py = path[i]
        if pivot == arr[px][py]:
            temp.append((px, py))
        else:
            if len(temp) >= 4:

                blowFlag = True
                for nx, ny in temp:
                    check(nx, ny)
                    arr[nx][ny] = 0

            temp = [(px, py)]
            pivot = arr[px][py]

    return blowFlag

def insertBall():
    temp = []
    px, py = path[1]
    pivot = arr[px][py]
    cnt = 1
    for i in range(2, len(path)):
        px, py = path[i]
        if pivot == arr[px][py]:
            cnt += 1

        else:
            temp.append(cnt)
            temp.append(pivot)
            pivot = arr[px][py]
            cnt = 1

    t = 0
    for i in range(1, len(path)):
        px, py = path[i]
        if t < len(temp):
            arr[px][py] = temp[t]
        else:
            arr[px][py] = 0

        t += 1


def show():
    for i in arr:
        print(i)
    print("###########")



n, m = map(int, input().split())
sx, sy = n // 2, n // 2
arr = [list(map(int, input().split())) for _ in range(n)]
path = getPath()


for i in range(m):
    d, s = map(int, input().split())
    d -= 1
    # show()
    getMagic(d, s)
    # show()
    moveBall()

    # show()
    while True:
        ret = getBlow()
        moveBall()
        if not ret:
            break

    # show()
    insertBall()
    # show()

answer = an + bn * 2 + cn * 3
print(answer)





