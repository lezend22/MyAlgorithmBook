import sys
from collections import defaultdict

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
p, dir, pc, depth, cnt = 1, 0, 0, 1, 0
dic = defaultdict(tuple)
x, y = n // 2, n // 2
answer = 0

xs = [[0, -1, -1, -2, -1, 1, 1, 2, 1],
      [2, 1, 0, 0, -1, -1, 0, 0, 1],
      [0, 1, 1, 2, 1, -1, -1, -2, -1],
      [-2, -1, 0, 0, 1, 1, 0, 0, -1]]


ys = [[-2, -1, 0, 0, 1, 1, 0, 0, -1],
      [0, -1, -1, -2, -1, 1, 1, 2, 1],
      [2, 1, 0, 0, -1, -1, 0, 0, 1],
      [0, 1, 1, 2, 1, -1, -1, -2, -1]]

perc = [0.05, 0.1, 0.07, 0.02, 0.01, 0.01, 0.07, 0.02, 0.1]


while p < (n*n):

    x = x + dx[dir]
    y = y + dy[dir]
    dic[p] = (x, y, dir)
    cnt += 1
    p += 1
    if cnt == depth:
        dir = (dir + 1) % 4
        cnt = 0
        pc += 1
        if pc == 2:
            pc = 0
            depth += 1

def splash(x, y, d):
    global answer
    pivot = arr[x][y]
    totalSpread = 0

    yvx = x + dx[d]
    yvy = y + dy[d]

    for i in range(9):
        nx = x + xs[d][i]
        ny = y + ys[d][i]
        # print(nx, ny)
        if 0 <= nx < n and 0 <= ny < n:
            amount = int(pivot * perc[i])
            arr[nx][ny] += amount
            totalSpread += amount

        else:
            amount = int(pivot * perc[i])
            totalSpread += amount
            answer += amount

    if 0 <= yvx < n and 0 <= yvy < n:
        arr[yvx][yvy] += pivot - totalSpread
    else:
        answer += pivot - totalSpread
    arr[x][y] = 0


for i in dic.keys():


    x, y, d = dic[i]
    if arr[x][y] == 0:
        continue
    # print(x, y, d)
    # print(arr)
    splash(x, y, d)
    # print(arr, answer)
print(answer)

