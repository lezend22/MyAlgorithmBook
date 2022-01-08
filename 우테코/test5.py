import sys
from collections import deque

def solution(rows, columns):
    flag = False
    flagCount = 0
    if rows == columns:
        flag = True
    arr = [[0] * columns for _ in range(rows)]
    visited = []
    queue = deque()
    value = 1
    dx = [0, 1]
    dy = [1, 0]
    arr[0][0] = value
    queue.append((0, 0))
    visited.append((0, 0))
    while queue and len(visited) != rows*columns:
        popleft = queue.popleft()
        x, y = popleft
        if flag == True and x == 0 and y == 0:
            if flagCount == 1:
                arr[x][y] -= (value-1)
                return arr
            flagCount += 1
        value += 1
        if arr[x][y] % 2:#홀
            nx = x+dx[0]
            ny = y+dy[0]
            if nx > rows-1:
                nx = nx % rows
            if ny > columns-1:
                ny = ny % columns

            arr[nx][ny] = value
            queue.append((nx, ny))
            if (nx, ny) not in visited:
                visited.append((nx, ny))
        else:#짝
            nx = x+dx[1]
            ny = y + dy[1]
            if nx > rows-1:
                nx = nx % rows
            if ny > columns-1:
                ny = ny % columns

            arr[nx][ny] = value
            queue.append((nx, ny))
            if (nx, ny) not in visited:
                visited.append((nx, ny))

    return arr

print(solution(3, 3))