import sys
from collections import deque

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def show():
    for i in arr:
        print(i)
    print()

def move_ball(start, other, dir, color):
    global arr
    nx, ny = start
    ox, oy = other
    rx, ry = -1, -1
    lim = 0
    if dir == 0 or dir == 2:
        lim = m
    if dir == 1 or dir == 3:
        lim = n
    for i in range(1, lim):
        nx = nx + dx[dir]
        ny = ny + dy[dir]

        if arr[nx][ny] == '#':
            rx = nx - dx[dir]
            ry = ny - dy[dir]
            break

        elif arr[nx][ny] == 'O':
            rx, ry = nx, ny
            break

        elif (nx, ny) == (ox, oy):
            rx = nx - dx[dir]
            ry = ny - dy[dir]
            break

    # print("RET POS:", rx, ry)
    return (rx, ry)


def wayTo(RL, BL, d):

    rx, ry = RL
    bx, by = BL
    if d == 0:
        tR = abs(0 - ry)
        tB = abs(0 - by)
        if tR <= tB:
            RL = move_ball(RL, BL, d, 'R')
            BL = move_ball(BL, RL, d, 'B')
        else:
            BL = move_ball(BL, RL, d, 'B')
            RL = move_ball(RL, BL, d, 'R')

    elif d == 1:
        tR = abs(0 - rx)
        tB = abs(0 - bx)
        if tR <= tB:
            RL = move_ball(RL, BL, d, 'R')
            BL = move_ball(BL, RL, d, 'B')
        else:
            BL = move_ball(BL, RL, d, 'B')
            RL = move_ball(RL, BL, d, 'R')

    elif d == 2:
        tR = abs(m - ry)
        tB = abs(m - by)
        if tR <= tB:
            RL = move_ball(RL, BL, d, 'R')
            BL = move_ball(BL, RL, d, 'B')
        else:
            BL = move_ball(BL, RL, d, 'B')
            RL = move_ball(RL, BL, d, 'R')

    elif d == 3:
        tR = abs(n - rx)
        tB = abs(n - bx)
        if tR <= tB:
            RL = move_ball(RL, BL, d, 'R')
            BL = move_ball(BL, RL, d, 'B')
        else:
            BL = move_ball(BL, RL, d, 'B')
            RL = move_ball(RL, BL, d, 'R')

    return RL, BL

if __name__ == '__main__':

    n, m = map(int, sys.stdin.readline().split())
    arr = []
    for i in range(n):
        l = list(map(str, sys.stdin.readline().rstrip()))
        arr.append(l)

    rx, ry, bx, by, hx, hy = 0, 0, 0, 0, 0, 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == "B":
                bx, by = i, j
                arr[i][j] = '.'
            if arr[i][j] == "R":
                rx, ry = i, j
                arr[i][j] = '.'
            if arr[i][j] == 'O':
                hx, hy = i, j

    RL, BL = ((rx, ry), (bx, by))
    queue = deque()
    queue.append((RL, BL, 0))
    visited = [(RL, BL)]
    flag = False
    ans = -1
    while queue:
        rL, bL, cnt = queue.popleft()
        # print("popleft", rL, bL)
        if rL == (hx, hy) and bL != (hx, hy):
            ans = cnt
            break
        for d in range(4):
            # print(d)
            RL, BL = wayTo(rL, bL, d)
            # print(RL, BL)
            if RL == (hx, hy) and BL != (hx, hy):
                flag = True
                ans = cnt + 1
                break
            if (RL, BL) not in visited and BL != (hx, hy):
                queue.append((RL, BL, cnt + 1))
                visited.append((RL, BL))
        if flag:
            break
    if ans > 10:
        ans = -1
    print(ans)



