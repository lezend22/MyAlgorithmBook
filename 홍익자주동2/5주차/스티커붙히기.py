import sys
from collections import deque

def findSpace(x, y, idx):
    nx, ny = x, y
    # print("findSpace")
    # print(nx, ny)
    # print("findSpace", x, y, idx)
    tempVisited = totalVisited[idx]
    # print(tempVisited)
    for i in tempVisited:
        # print(i)
        a, b = i
        nx, ny = nx + a, ny + b
        if nx >= n or ny >= m:
            return False
        if arr[nx][ny] == 1:
            return False
        nx, ny = x, y
    ##fill Space
    # print("fill space")
    # print(totalVisited[idx])
    nx, ny = x, y
    for i in tempVisited:
        a, b = i
        nx, ny = nx + a, ny + b
        # print(nx, ny)
        arr[nx][ny] = 1
        nx, ny = x, y

    return True


def findSpot(r, c, idx):

    # print("r=", r, "c=", c)
    # print("n=", n, "m=", m)
    for i in range(n):
        if i + r > n:
            continue
        for j in range(m):
            if j + c > m:
                continue
            x, y = i, j
            # print(x, y)
            # print("here", x, y)
            if not findSpace(x, y, idx):
                continue
            else:
                # print("here")
                return True

def dfs(temp, r, c, idx):

    queue = deque()
    visited = []
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    x, y = -1, -1
    # print(temp)
    flag = False
    for i in range(r):
        if not flag:
            for j in range(c):
                if temp[i][j] == 'ssg':
                    x, y = i, j
                    flag = True
                    # print(x, y)
                    break
        else:
            break
    queue.append((x, y))
    visited.append((x, y))

    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < r and 0 <= ny < c and temp[nx][ny] == 'ssg' and (nx, ny) not in visited:
                queue.append((nx, ny))
                visited.append((nx, ny))
    # print("visited", visited)

    totalVisited[idx] = visited
    # print("totalVisited", totalVisited)

    return None

def getTurn(idx, c):
    # print("getTurn")
    length = c
    temp = totalVisited[idx]
    for i in range(len(temp)):
        x, y = temp[i]
        # print("cnt", cnt)
        nx = y
        ny = (length - 1) - x
        temp[i] = (nx, ny)

if __name__ == '__main__':

    n, m, k = map(int, sys.stdin.readline().split())
    arr = [[0] * m for _ in range(n)]

    cast = []
    totalVisited = [[] for _ in range(k)]
    for i in range(k):
        # print("######", i, "#######")
        # print(arr)
        r, c = map(int, sys.stdin.readline().split())
        temp = [list(sys.stdin.readline().split()) for _ in range(r)]
        dfs(temp, r, c, i)
        # print(r, c, n, m)
        # print(totalVisited[i])
        cnt = 0
        flag = False
        while cnt < 4:

            if r > n or c > m:
                r, c = c, r
                getTurn(i, c)
                # print(totalVisited[i])
                cnt += 1
                continue

            cnt += 1
            # if findSpot is True
            if findSpot(r, c ,i):
                # print("getOut")
                flag = True
                break
            else:
                r,c = c, r
                getTurn(i, c)

        # print(arr)
        if flag:
            continue
    result = 0
    for i in arr:
        result += sum(i)

    print(result)