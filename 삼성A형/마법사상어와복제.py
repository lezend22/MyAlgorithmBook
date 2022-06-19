import sys
from collections import deque, defaultdict

m, s = map(int, input().split())
arr = [[[] for _ in range(5)] for _ in range(5)]
for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a][b].append(c)
sx, sy = map(int, input().split())

fx = [0, -1, -1, -1, 0, 1, 1 ,1]
fy = [-1, -1, 0, 1, 1, 1, 0, -1]

def move():
    temp = [[[] for _ in range(5)] for _ in range(5)]
    for x in range(1, 5):
        for y in range(1, 5):
            if arr[x][y] != []:
                for node in arr[x][y]:
                    # print("this", node, x, y)
                    if node == -5:
                        temp[x][y].append(node)
                        continue
                    mov = node - 1
                    flag = False
                    for i in range(8):
                        if mov < 0:
                            mov = 8 + mov
                        nx = x + fx[mov]
                        ny = y + fy[mov]
                        # print(nx, ny)

                        ### nx, ny and 오퍼레이션 때매 안됨 다음엔 이거 확인
                        if 1 <= nx < 5 and 1<= ny <5 and not (nx == sx and ny == sy) and smellPos[nx][ny] == 0:
                            # print("goes", mov+ssg, nx, ny, ",,,,,")
                            temp[nx][ny].append(mov + 1)
                            flag = True
                            break
                        mov -= 1
                    if not flag:
                        temp[x][y].append(node)
    return temp

def sharkMove(sx, sy, cnt, path):
    global poss, pivot, visited

    # print(sx, sy)
    if len(path) == 3:
        if cnt > pivot:
            # print("this",path, cnt)
            poss.append((path, cnt))
            pivot = cnt
        return

    for i in range(4):
        nx = sx + dx[i]
        ny = sy + dy[i]
        if 1 <= nx < 5 and 1 <= ny < 5:

            if not visited[nx][ny]:
                visited[nx][ny] = True
                sharkMove(nx, ny, cnt + len(arr[nx][ny]), path + [(nx, ny)])
                visited[nx][ny] = False
            else:
                sharkMove(nx, ny, cnt, path + [(nx, ny)])


def deleteFish(sharkPath):
    for path in sharkPath:
        a, b = path
        if arr[a][b] != []:
            arr[a][b] = []
            smellPos[a][b] = 3


def deleteSmell(smellPos):

    for i in range(1, 5):
        for j in range(1, 5):
            if smellPos[i][j] != 0:
                smellPos[i][j] -= 1

def copyFish(temp):

    for i in range(1, 5):
        for j in range(1, 5):
            if temp[i][j] == []:
                continue
            arr[i][j] += temp[i][j]

smellPos = [[0] * 5 for _ in range(5)]
for tc in range(s):

    temp = arr[:]

    arr = move()

    poss = []
    pivot = -1
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    visited = [[False] * 5 for _ in range(5)]
    sharkMove(sx, sy, 0, [])
    # poss.sort(key= lambda x:x[ssg])
    sharkPath = poss[-1][0]

    sx, sy = sharkPath[-1]

    deleteFish(sharkPath)
    # print(smellPos)
    deleteSmell(smellPos)

    copyFish(temp)


answer = 0
smellNum = 0
for i in range(1, 5):
    for j in range(1, 5):
        if arr[i][j] == []:
            continue
        answer += len(arr[i][j])

print(answer)
