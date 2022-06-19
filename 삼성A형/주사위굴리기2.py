import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().split())
arr = [[0] * (m+1)]
for _ in range(n):
    tmp = [0] + list(map(int, sys.stdin.readline().split()))
    arr.append(tmp)

dice = [[0, 2, 0], [4, 1, 3], [0, 5, 0], [0, 6, 0]]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 0: north, ssg: east, 2:south, 3:west

def east():
    tmp = dice[1][0]
    dice[1][0] = dice[3][1]
    tmp2 = dice[1][1]
    dice[1][1] = tmp
    tmp = dice[1][2]
    dice[1][2] = tmp2
    dice[3][1] = tmp

def west():
    tmp = dice[1][1]
    dice[1][1] = dice[1][2]
    tmp2 = dice[1][0]
    dice[1][0] = tmp
    tmp = dice[3][1]
    dice[3][1] = tmp2
    dice[1][2] = tmp

def north():
    tmp = dice[0][1]
    dice[0][1] = dice[1][1]
    tmp2 = dice[3][1]
    dice[3][1] = tmp
    tmp = dice[2][1]
    dice[2][1] = tmp2
    dice[1][1] = tmp

def south():
    tmp = dice[1][1]
    dice[1][1] = dice[0][1]
    tmp2 = dice[2][1]
    dice[2][1] = tmp
    tmp = dice[3][1]
    dice[3][1] = tmp2
    dice[0][1] = tmp

def move(movNum, curr):
    x, y = curr
    nx = x + dx[movNum]
    ny = y + dy[movNum]
    if 1 <= nx < n+1 and 1 <= ny < m+1:
        if movNum == 0:
            north()
        elif movNum == 1:
            east()
        elif movNum == 2:
            south()
        elif movNum == 3:
            west()
    else:
        movNum = movNum - 2
        if movNum < 0:
            movNum = 4 + movNum
        nx = x + dx[movNum]
        ny = y + dy[movNum]
        if movNum == 0:
            north()
        elif movNum == 1:
            east()
        elif movNum == 2:
            south()
        elif movNum == 3:
            west()

    return nx, ny, movNum

answer = 0
cnt = 0
x, y = 1, 1
movNum = 1
while cnt < k:

    # print(x, y, movNum)
    x, y, movNum = move(movNum, (x, y))
    # print(x, y, movNum)
    a = dice[3][1]
    b = arr[x][y]
    if a > b:
        movNum += 1
        if movNum > 3:
            movNum = movNum % 4
    elif a < b:
        movNum -= 1
        if movNum < 0:
            movNum = 4 + movNum
    elif a == b:
        pass
    cnt += 1

    # check points
    pivot = arr[x][y]
    nodeCnt = 1
    queue = deque()
    queue.append((x, y))
    visited = [(x, y)]
    while queue:
        qx, qy = queue.popleft()

        for i in range(4):
            nx = qx + dx[i]
            ny = qy + dy[i]
            if 0 <= nx < n+1 and 0 <= ny < m+1 and arr[nx][ny] == pivot and (nx, ny) not in visited:
                nodeCnt += 1
                queue.append((nx, ny))
                visited.append((nx, ny))

    answer += (pivot * nodeCnt)
    # print(answer)

print(answer)








