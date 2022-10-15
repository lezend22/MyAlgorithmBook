import heapq

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

vx = [-1, -1, 1, 1]
vy = [-1, 1, 1, -1]

def grow():

    for i in range(n):
        for j in range(n):
            if arr[i][j] == -1:
                continue

            if arr[i][j]:
                x, y = i, j
                cnt = 0
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n:
                        if arr[nx][ny] == -1:
                            continue
                        if arr[nx][ny]:
                            cnt += 1

                arr[i][j] += cnt


def spread():
    ret = [x[:] for x in arr]

    for i in range(n):
        for j in range(n):
            if arr[i][j] == -1:
                continue

            if arr[i][j]:

                temp = []
                x, y = i, j
                cnt = 0
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n:
                        if arr[nx][ny] == 0 and not zone[nx][ny]:
                            cnt += 1
                            temp.append((nx, ny))

                if cnt == 0:
                    continue

                val = arr[i][j] // cnt
                for nx, ny in temp:
                    ret[nx][ny] += val


    return ret


def getKill():

    total = []


    for i in range(n):
        for j in range(n):
            if arr[i][j] == -1:
                continue
            if arr[i][j]:
                x, y = i, j
                killed = arr[i][j]
                dmove = [0, 0, 0, 0]
                for s in range(1, k+1):
                    for d in range(4):
                        if dmove[d]:
                            continue
                        nx = x + vx[d] * s
                        ny = y + vy[d] * s
                        if 0 <= nx < n and 0 <= ny < n:
                            if arr[nx][ny] == -1 or arr[nx][ny] == 0:
                                dmove[d] = 1
                                continue

                            if arr[nx][ny]:
                                killed += arr[nx][ny]

                heapq.heappush(total, (-killed, i, j))

    # print(total)
    if not total:
        return 0, []

    _, x, y = heapq.heappop(total)
    # print(x, y)
    ret = arr[x][y]
    arr[x][y] = 0  #박멸
    zone[x][y] = c
    dmove = [0, 0, 0, 0]
    exp = [(x, y)]

    for s in range(1, k+1):
        for d in range(4):
            if dmove[d]:
                continue

            nx = x + vx[d] * s
            ny = y + vy[d] * s
            # print("try", nx, ny)
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == -1:
                    # print("get in", nx, ny)
                    dmove[d] = 1
                    continue

                if arr[nx][ny] == 0:
                    zone[nx][ny] = c
                    exp.append((nx, ny))
                    dmove[d] = 1
                    continue

                if arr[nx][ny]:
                    # print("SUCCES", nx, ny)
                    # print(nx, ny)
                    ret += arr[nx][ny]
                    arr[nx][ny] = 0  ## 박멸
                    zone[nx][ny] = c
                    exp.append((nx, ny))

    return ret, exp

def decreaseZone(exp):
    for i in range(n):
        for j in range(n):
            if zone[i][j] and (i, j) not in exp:
                zone[i][j] -= 1


def show():
    for i in arr:
        print(i)
    print("#########")

def show2():
    for i in zone:
        print(i)
    print("@@@@@@@@")

n, m, k, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
zone = [[0] * n for _ in range(n)]
answer = 0
for _ in range(m):

    # show()
    grow()
    # show()
    arr = spread()
    # show()
    ret, exp = getKill()
    answer += ret
    # show()
    decreaseZone(exp)
    # show2()

    # break

print(answer)