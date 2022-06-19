
r, c, m = map(int, input().split())
arr = [[[] for _ in range(c)] for _ in range(r)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
catchShark = 0
for _ in range(m):
    r1, c1, s, d, z = map(int, input().split())
    arr[r1-1][c1-1] = [s, d-1, z]

def reverseDir(d):
    if d == 3:
        return 2
    elif d == 2:
        return 3
    elif d == 1:
        return 0
    elif d == 0:
        return 1

def fishing(y):
    global catchShark
    for i in range(r):
        if arr[i][y]:
            catchShark += arr[i][y][2]
            arr[i][y] = []
            return

def sharkMove():
    temp = [[[] for _ in range(c)] for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if arr[x][y]:
                # print(x, y, arr[x][y])
                nx, ny = x, y
                ns, nd, dz = arr[x][y]
                for _ in range(ns):
                    nx = nx + dx[nd]
                    ny = ny + dy[nd]
                    if not (0 <= nx < r and 0 <= ny < c):
                        nx -= dx[nd]
                        ny -= dy[nd]
                        nd = reverseDir(nd)
                        nx += dx[nd]
                        ny += dy[nd]
                if temp[nx][ny]:
                    # print("already exist",nx, ny, temp[nx][ny], arr[x][y])
                    p_n = temp[nx][ny][2]
                    c_n = arr[x][y][2]
                    if p_n < c_n:
                        temp[nx][ny] = [ns, nd, dz]
                else:
                    # print("put on temp", nx, ny, arr[x][y])
                    temp[nx][ny] = [ns, nd, dz]

    return temp

k = 0
while k < c:
    # print(arr)
    fishing(k)
    # print(arr)
    arr = sharkMove()
    # print(arr)
    k += 1
    # print("#########")

print(catchShark)