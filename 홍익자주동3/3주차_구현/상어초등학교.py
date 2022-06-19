import sys
from collections import deque

n = int(sys.stdin.readline())
dic = {}
for _ in range(n*n):
    temp = list(map(int, sys.stdin.readline().split()))
    dic[temp[0]] = temp[1:]

sit = [[0] * n for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def checkVacant(i, j):

    cnt = 0
    x, y = i, j
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and sit[nx][ny] == 0:
            cnt += 1
    return cnt

def checkLike(i, j, k):

    cnt = 0
    x, y = i, j
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and sit[nx][ny] in dic[k]:
            cnt += 1

    return cnt

def getSit(k):

    maxSpace = -1
    maxLike = -1
    x, y = -1, -1
    posPos = []
    for i in range(n):
        for j in range(n):
            if sit[i][j] != 0:
                continue

            w = checkLike(i, j, k)
            if maxLike < w:
                posPos = []
                maxLike = w
                x, y = i, j
                posPos.append((i, j))
            elif maxLike == w:
                posPos.append((i, j))

    if len(posPos) == 1:
        x, y = posPos[0]
        return x, y

    #7, 2위치에서 막힘. thru False일때 아무것도 안하는것이 문제 위에서 가능한 부분에서 밑에서 골라야함.
    for node in posPos:
        i, j = node
        if sit[i][j] == 0:
            v = checkVacant(i, j)
            if maxSpace < v:
                maxSpace = v
                x, y = i, j

    return x, y



if __name__ == '__main__':

    for i in dic.keys():
        x, y = getSit(i)
        sit[x][y] = i
        # print(sit)

    ans = 0
    for i in range(n):
        for j in range(n):
            ret = checkLike(i, j, sit[i][j])
            if ret == 0:
                continue
            elif ret == 1:
                ans += 1
            elif ret == 2:
                ans += 10
            elif ret == 3:
                ans += 100
            elif ret == 4:
                ans += 1000
    print(ans)
