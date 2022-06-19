from collections import deque

n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def seperate(group):

    for g_r in group:
        populate, path = g_r[0], g_r[1]
        length = len(path)
        for x, y in path:
            arr[x][y] = populate // length


def findBorder(x, y):

    # print(x, y)
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    totalPop = arr[x][y]
    temp = [(x, y)]
    while queue:
        x, y, = queue.popleft()
        p_n = arr[x][y]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                c_n = arr[nx][ny]
                if l <= abs(p_n - c_n) <= r:
                    totalPop += arr[nx][ny]
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    temp.append((nx, ny))

    return [totalPop, temp]



def openBorder():
    group = []
    for x in range(n):
        for y in range(n):
            if not visited[x][y]:
                t = findBorder(x, y)
                if len(t[1]) > 1:
                    group.append(t)

    return group

days = 0
while True:

    visited = [[False] * n for _ in range(n)]
    border = openBorder()
    # print(border)
    if border:
        seperate(border)
    else:
        break
    days += 1

print(days)