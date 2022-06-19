import copy

arr = [[] for _ in range(4)]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

for i in range(4):
    tp = list(map(int, input().split()))
    fish = []
    for j in range(4):
        fish.append([tp[2*j], tp[2*j+1]-1])
    arr[i] = fish

answer = 0

def dfs(sx, sy, score, arr):
    global answer
    score += arr[sx][sy][0]
    answer = max(answer, score)
    arr[sx][sy][0] = 0
    sharkDir = arr[sx][sy][1]

    for pivot in range(1, 17):
        fx, fy = -1, -1
        for i in range(4):
            for j in range(4):
                if arr[i][j][0] == pivot:
                    fx, fy = i, j
                    break
        if fx == -1 and fy == -1:
            continue
        fishDir = arr[fx][fy][1]
        for i in range(8):
            nd = (fishDir + i) % 8
            nx = fx + dx[nd]
            ny = fy + dy[nd]
            if 0 <= nx < 4 and 0 <= ny < 4 and not (nx == sx and ny == sy):
                arr[fx][fy][1] = nd
                arr[fx][fy], arr[nx][ny] = arr[nx][ny], arr[fx][fy]
                break

    for i in range(1, 5):
        nx = sx + dx[sharkDir] * i
        ny = sy + dy[sharkDir] * i
        if 0 <= nx < 4 and 0 <= ny < 4 and arr[nx][ny][0] > 0:
            dfs(nx, ny, score, copy.deepcopy(arr))

dfs(0, 0, 0, arr)
print(answer)

