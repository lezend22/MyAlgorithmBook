from collections import deque
from itertools import combinations
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = []
group = []

def bfs(loc):
    global visited
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    a, b = loc
    pivot = arr[a][b]
    queue = deque()
    queue.append(loc)
    tempV = {loc}

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == pivot and (nx, ny) not in tempV and (nx, ny) not in visited:
                tempV.add((nx, ny))
                queue.append((nx, ny))
                visited.append((nx, ny))

    ret = [pivot, tempV]
    return ret

def divide():
    for i in range(n):
        for j in range(n):
            if (i, j) not in visited:
                ret = bfs((i, j))
                group.append(ret)


def getPoint():
    ret = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    c = list(combinations(group, 2))
    for i in c:

        cnt = 0
        a1, a2 = i
        p1, p2 = a1[0], a2[0]
        a1, a2 = a1[1], a2[1]
        for j in a1:
            x1, y1 = j
            for t in range(4):
                nx = x1 + dx[t]
                ny = y1 + dy[t]
                if (nx, ny) in a2:
                    cnt += 1

        la = len(a1)
        lb = len(a2)
        # print("here", la, lb)
        ret += (la + lb) * p1 * p2 * cnt
    return ret


def crossRotate():

    temp = [[0] * n for _ in range(n)]
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    move = [(1, -1), (1, 1), (-1, 1), (-1, -1)]
    sx, sy = n // 2, n // 2
    path = [(sx, sy)]
    temp[sx][sy] = arr[sx][sy]
    l = 1
    while l <= sx:
        for d in range(4):
            nx = sx + dx[d] * l
            ny = sy + dy[d] * l
            path.append((nx, ny))
            px, py = move[d]
            nnx = nx + px * l
            nny = ny + py * l
            temp[nnx][nny] = arr[nx][ny]
        l += 1

    return path, temp
    # for i in path:
    #     a, b = i
    #     arr[a][b] = temp[a][b]

def rotate(arr):
    tn = len(arr)
    temp = [[0] * tn for _ in range(tn)]
    for i in range(tn):
        for j in range(tn):
            temp[i][j] = arr[tn-1-j][i]

    return temp


def clockWiseRotate():
    sx = n // 2
    rot = [(0, sx, 0, sx), (sx+1, n, 0, sx), (0, sx, sx+1, n), (sx+1, n, sx+1, n)]
    l1 = sx
    temp = [[0] * n for _ in range(n)]
    for i in rot:
        x, ex, y, ey = i
        tmp = [row[y:ey] for row in arr[x:ex]]
        tmp = rotate(tmp)
        k1, k2 = 0, 0

        for a in range(x, ex):
            k2 = 0
            for b in range(y, ey):
                arr[a][b] = tmp[k1][k2]
                k2 += 1
            k1 += 1

def show():
    for i in arr:
        print(i)
    print("###########")

count = 0
answer = 0
while count < 4:
    visited = []
    group = []
    # print(count)
    divide()
    ptr = getPoint()
    # print(ptr)
    answer += ptr
    # show()
    path, tmp = crossRotate()
    # show()
    clockWiseRotate()
    # show()
    for i in path:
        a1, b1 = i
        arr[a1][b1] = tmp[a1][b1]
    # show()
    count += 1

print(answer)