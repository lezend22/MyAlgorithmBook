arr = []
answer, flag = 0, False
alloc, blloc = [], []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def distance(x, y, target):
    tx, ty = target
    ret = abs(tx - x) + abs(ty - y)
    return ret

def moveAway(pivot, target):
    global answer
    px, py = pivot
    rx, ry = -1, -1
    maxDist = 0
    poss = 0
    for i in range(4):
        nx = px + dx[i]
        ny = py + dy[i]
        if 0 <= nx < len(arr) and 0 <= ny < len(arr[0]) and arr[nx][ny] == 1:
            poss += 1
            dist = distance(nx, ny, target)
            if maxDist <= dist:
                maxDist = dist
                rx, ry = nx, ny
    if poss == 0:
        return -1, -1
    arr[px][py] = 0
    answer += 1
    return rx, ry

def moveTo(pivot, target):
    global answer
    minDist = 1e9
    rx, ry = -1, -1
    sx, sy = pivot
    poss = 0
    for i in range(4):
        nx = sx + dx[i]
        ny = sy + dy[i]
        if 0 <= nx < len(arr) and 0 <= ny < len(arr[0]) and arr[nx][ny] == 1:
            poss += 1
            dist = distance(nx, ny, target)
            if minDist > dist:
                minDist = dist
                rx, ry = nx, ny
    if poss == 0:
        return -1, -1
    arr[sx][sy] = 0
    answer += 1
    return rx, ry

def check(alloc, blloc):
    global flag
    ax, ay = alloc
    bx, by = blloc
    if alloc == [-1, -1]:
        flag = True
        return False
    if blloc == [-1, -1]:
        return False
    if arr[ax][ay] == 0:
        flag = True
        return False
    if arr[bx][by] == 0:
        return False

    return True


def solution(board, aloc, bloc):
    global arr, alloc, blloc, answer
    arr = [item[:] for item in board]
    # print(arr)
    alloc,blloc = aloc, bloc
    while True:

        ax, ay = moveTo(alloc, blloc)
        alloc = [ax, ay]
        if not check(alloc, blloc):
            # print(answer)
            break
        # print("Amove", ax, ay)

        bx, by = moveAway(blloc, alloc)
        blloc = [bx, by]
        if not check(alloc, blloc):
            # print(answer)
            return answer
        # print("Bmove", bx, by)

    if flag:
        # print("init all####")
        answer = 0
        alloc, blloc, arr = aloc, bloc, board
        while True:
            ax, ay, = moveTo(alloc, blloc)
            alloc = [ax, ay]
            # print("Amove", ax, ay)
            if not check(alloc, blloc):
                # print(answer)
                return answer

            bx, by = moveTo(blloc, alloc)
            blloc = [bx, by]
            if not check(alloc, blloc):
                # print(answer)
                return answer
            # print("Bmove", bx, by)

    return answer

print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2]))
