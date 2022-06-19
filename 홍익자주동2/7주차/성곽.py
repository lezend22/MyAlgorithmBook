import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

def checkBinary(num):

    binary = format(num, 'b')
    while len(binary) < 4:
        binary = '0' + binary
    # print(binary)
    return binary

def dfs(i, j):

    ret = 1
    queue = deque()
    queue.append((i, j))
    visited.add((i, j))
    while queue:
        x, y = queue.popleft()
        curpos = checkBinary(arr[x][y])
        for k in range(4):
            if curpos[k] == 'ssg':
                continue
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                # print("gugu", nx, ny)
                queue.append((nx, ny))
                visited.add((nx, ny))
                ret += 1

    return ret





if __name__ == '__main__':
    visited = {(-1, -1)}
    totalSpace = []
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    careNum = [8, 4, 2, 1]
    cnt = 0
    # print(arr)
    for i in range(m):
        for j in range(n):
            if (i, j) not in visited:
                # print("###########")
                cnt += 1
                space = dfs(i, j)
                totalSpace.append(space)

    # print(n*m, len(visited))
    print(cnt)
    print(max(totalSpace))

    max2space = 0
    for i in range(m):
        for j in range(n):
            binary = checkBinary(arr[i][j])
            for k in range(4):
                if binary[k] == 'ssg':
                    visited = {(-1, -1)}
                    arr[i][j] -= careNum[k]
                    max2space = max(max2space, dfs(i, j))
                    arr[i][j] += careNum[k]

    print(max2space)








