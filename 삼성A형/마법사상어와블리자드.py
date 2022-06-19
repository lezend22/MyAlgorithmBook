n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
magic = [list(map(int, input().split())) for _ in range(m)]


ex = [-1, 1, 0, 0]
ey = [0, 0, -1, 1]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


p, dir, cnt, pc, depth = 1, 0, 0, 0, 1
x, y = n // 2, n // 2
dic = {}
while p <= (n*n)-1:
    x = x + dx[dir]
    y = y + dy[dir]
    dic[p] = (x, y)
    cnt += 1
    p += 1
    if cnt == depth:
        dir = (dir + 1) % 4
        cnt = 0
        pc += 1
        if pc == 2:
            pc = 0
            depth += 1

an, bn, cn = 0, 0, 0
def smash(x, y):

    for _ in range(s):
        x = x + ex[dir]
        y = y + ey[dir]

        if 0<=x<n and 0<=y<n:
            arr[x][y] = 0

def getPull(i):
    global moveFlag
    while i+1 <= (n*n)-1:
        cx, cy, = dic[i]
        nx, ny = dic[i+1]
        if arr[cx][cy] != 0 and arr[nx][ny] != 0:
            moveFlag = True
        arr[cx][cy] = arr[nx][ny]
        i += 1

    lx, ly = dic[i]
    arr[lx][ly] = 0

def move():
    global moveFlag
    tale = findTale()
    for i in dic.keys():
        if i == tale:
            return
        x, y, = dic[i]
        if arr[x][y] == 0:
            getPull(i)

def countExplodeNum(num, length):
    global an, bn, cn
    if num == 1:
        an += length
    elif num == 2:
        bn += length
    elif num == 3:
        cn += length


def explode():
    pivot = -1
    cnt = 1
    visited = []
    flag = False
    for i in dic.keys():
        x, y = dic[i]
        if arr[x][y] != pivot:
            if flag:
                # print(pivot, cnt)
                for node in visited:
                    x, y = node
                    arr[x][y] = 0
                    # print("explode", pivot, len(visited))
                countExplodeNum(pivot, len(visited))
                flag = False
            # print("pivot change", pivot)
            cnt = 1
            pivot = arr[x][y]
            visited = [(x, y)]
        else:
            cnt += 1
            visited.append((x, y))
        if cnt >= 4:
            flag = True

def change():
    ret = [[0] * (n) for _ in range(n)]
    pivot, cnt, startP, gn = -1, 0, 0, -1
    flag = False
    for i in dic.keys():
        x, y = dic[i]
        if arr[x][y] != pivot:
            if flag:
                if startP >= (n*n)-1:
                    return ret
                gcnt = cnt
                startP += 1
                px, py, = dic[startP]
                ret[px][py] = gcnt
                startP += 1
                px, py = dic[startP]
                ret[px][py] = gn

            pivot = arr[x][y]
            gn = pivot
            cnt = 1
            flag = True
        else:
            flag = True
            cnt += 1

    return ret

def findTale():

    keys = list(dic.keys())
    for i in range(len(keys)-1, -1, -1):
        x, y = dic[keys[i]]
        if arr[x][y] == 0:
            continue
        else:
            return i + 2


sx, sy = n // 2, n // 2
x, y = sx, sy
for i in range(m):
    d, s, = magic[i]
    dir = d - 1
    # print(arr)
    smash(sx, sy)
    # print(arr)

    while True:
        moveFlag = False
        # print("temp", temp)
        move()
        # print(arr)
        explode()
        if not moveFlag:
            break
        # print("arr", arr)

    arr = change()

print(an + bn*2 + cn*3)
