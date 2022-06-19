import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(n)]
inp = list(map(int, sys.stdin.readline().split()))
for i in range(n):
    arr[i].append(inp[i])
queue = deque(arr)

def addFish():
    minA = min(queue)[0]
    # print(minA)
    for i in range(len(queue)):
        if queue[i][0] == minA:
            queue[i][0] += 1


def putOn():
    popleft = queue.popleft()
    for i in popleft:
        queue[0].append(i)
    # print(queue)

def airTurn():
    while True:
        until = -1
        for i in range(len(queue)-1, -1, -1):
            if len(queue[i]) >= 2:
                if len(queue)-1 - i < len(queue[i]):
                    return
                until = i
                break
        tmp = deque()
        for i in range(until+1):
            popleft = queue.popleft()
            tmp.appendleft(popleft)

        for popleft in tmp:
            k = 0
            for i in popleft:
                queue[k].append(i)
                k += 1

def fishDivide():
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    tempArr = [[0] * (len(queue[0])) for _ in range(len(queue))]

    for x in range(len(queue)):
        for y in range(len(queue[x])):
            curr = queue[x][y]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < len(queue) and 0 <= ny < len(queue[x]):
                    # print("he",x, y, len(queue), len(queue[x]))
                    # print(nx, ny)
                    try:
                        gap = queue[nx][ny] - curr
                    except:
                        continue
                    d = abs(gap) // 5
                    # print("check", x, y, nx, ny, d)
                    if d > 0:
                        if queue[nx][ny] > queue[x][y]:
                            tempArr[nx][ny] -= d
                            tempArr[x][y] += d
                        else:
                            tempArr[nx][ny] += d
                            tempArr[x][y] -= d

    for x in range(len(tempArr)):
        for y in range(len(tempArr[x])):
            try:
                queue[x][y] += (tempArr[x][y] // 2)
            except:
                continue

def reLine():
    tmp = []
    while queue:
        popleft = queue.popleft()
        for j in popleft:
            tmp.append(j)

    for i in tmp:
        queue.append([i])

def turnHalf():

    for _ in range(2):
        length = len(queue) // 2 - 1
        tmp = deque()
        i = 0
        while i <= length:
            popleft = queue.popleft()
            t = []
            while popleft:
                pop = popleft.pop()
                t.append(pop)
            tmp.appendleft(t)
            i += 1

        k = 0
        for node in tmp:
            for j in node:
                queue[k].append(j)
            k += 1



cnt = 0
while max(queue)[0] - min(queue)[0] > k:
    cnt += 1
    addFish()
    # print(queue)
    putOn()
    # print(queue)
    airTurn()
    # print(queue)
    fishDivide()
    # print(queue)
    reLine()
    # print(queue)
    turnHalf()
    # print(queue)
    fishDivide()
    # print(queue)
    reLine()
    # print(queue)

print(cnt)