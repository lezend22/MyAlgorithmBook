
n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
shark = [0] + list(map(int, input().split()))
print(shark)
priority = [[0]]
for _ in range(m):
    temp = [list(map(int, input().split())) for _ in range(4)]
    priority.append(temp)
smell = [[0] * n for _ in range(n)]
whoSmell = [[0] * n for _ in range(n)]
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

def specificRule(x, y, pivot, dir):

    posDir = priority[pivot][dir-1]
    for d in posDir:
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n:
            return d

def findSameSmell(x, y, pivot):

    posDir = []
    for i in range(1, 5):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and whoSmell[nx][ny] == pivot:
            posDir.append(i)
    return posDir

def getEmptyDir(x, y):
    dir = -1
    for i in range(1, 5):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and smell[nx][ny] == 0:
            dir = i
            break
    if dir == -1:
        print("error")
    return dir

def findDir():
    tempSmell = [item[:] for item in smell]
    ret = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if arr[x][y] != 0:
                pivot = arr[x][y]
                print("pivot start", pivot, x, y)
                dir = shark[pivot]

                emptyCnt = 0
                for i in range(1, 5):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n:
                        print(nx, ny, smell[nx][ny])
                        if smell[nx][ny] == 0:
                            emptyCnt += 1
                print("empt", pivot, emptyCnt)
                if emptyCnt == 1:
                    dir = getEmptyDir(x, y)
                    pass
                elif emptyCnt > 1:
                    print("here empty many", pivot, dir)
                    dir = specificRule(x, y, pivot, dir)
                elif emptyCnt == 0:
                    posDir = findSameSmell(x, y, pivot)
                    if len(posDir) > 1:
                        dir = specificRule(x, y, pivot, dir)
                    else:
                        print(posDir)
                        dir = posDir[0]

                nnx, nny = x + dx[dir], y + dy[dir]
                print(pivot, nnx, nny, dir)
                if ret[nnx][nny] != 0:
                    if ret[nnx][nny] > pivot:
                        ret[nnx][nny] = pivot
                        whoSmell[nnx][nny] = pivot
                        shark[pivot] = dir
                else:
                    ret[nnx][nny] = pivot
                    shark[pivot] = dir

                tempSmell[x][y] -= 1
                tempSmell[nnx][nny] = k
                # print(arr)
    return ret, tempSmell

def smellGone():
    for i in range(n):
        for j in range(n):
            if smell[i][j] == 0:
                whoSmell[i][j] = 0

def shitSmell():
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                smell[i][j] = k
                whoSmell[i][j] = arr[i][j]

def checkBreak():
    pos = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                pos.append(arr[i][j])

    if len(pos) == 1:
        if pos[0] == 1:
            return True
    else:
        return False

print(smell)
shitSmell()
print(smell)
cnt = 0
while True:
    if checkBreak():
        break
    print(smell)
    print("arr", arr)
    arr, smell = findDir()
    print("arr", arr)
    smellGone()
    # print(smell)
    cnt += 1
    print("#############")
print(cnt)