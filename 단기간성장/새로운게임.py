import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
horses = [[deque() for _ in range(n)] for _ in range(n)]
poss = {}
for i in range(1, k + 1):
    a, b, c = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    c -= 1
    horses[a][b].append([i, c])
    poss[i] = (a, b)

turn = 0
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def inverse(d):
    if d == 0:
        return 1
    elif d == 1:
        return 0
    elif d == 2:
        return 3
    elif d == 3:
        return 2

def getMove(x, y, d, fflag):
    # 0 흰, 1 빨, 2 파
    nx = x + dx[d]
    ny = y + dy[d]
    temp = horses[x][y]
    flag = False

    if not (0 <= nx < n and 0 <= ny < n):
        if fflag:
            return
        d = inverse(d)
        nx = x + dx[d]
        ny = y + dy[d]
        horses[x][y][0][1] = d
        flag = True

    if arr[nx][ny] == 0:
        for p in temp:
            poss[p[0]] = (nx, ny)
            horses[nx][ny].append(p)
        horses[x][y] = deque()

    elif arr[nx][ny] == 1:
        temp = list(temp)[::-1]
        for p in range(len(temp)):
            p_ = temp[p]
            poss[p_[0]] = (nx, ny)
            horses[nx][ny].append(p_)
        horses[x][y] = deque()

    elif not flag and arr[nx][ny] == 2:
        d = inverse(d)
        nnx, nny = x + dx[d], y + dy[d]
        horses[x][y][0][1] = d
        if 0 <= nnx < n and 0 <= nny < n and arr[nnx][nny] != 2:
            getMove(x, y, d, True)


def move(turn):
    for i in range(1, k+1):
        if check():
            answer = turn
            return
        x, y, = poss[i]
        # print(x, y, i)
        # show()
        pivot = horses[x][y][0]
        if pivot[0] == i:
            getMove(x, y, pivot[1], False)
        else:
            continue

def check():
    for i in range(n):
        for j in range(n):
            if len(horses[i][j]) >= 4:
                return True

    return False

def show():
    for i in horses:
        print(i)
    print("########")

answer = -1
while turn < 1000:

    if check():
        answer = turn
        break
    turn += 1
    move(turn)

print(answer)