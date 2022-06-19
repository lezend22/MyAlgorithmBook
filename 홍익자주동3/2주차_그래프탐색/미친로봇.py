import sys

# 바보같이 ssg-(안되는거)로 접근했다가 해맴
# e, w, s, n
arr = list(map(int, sys.stdin.readline().split()))
k = arr[0]
arr = arr[1:]
for i in range(len(arr)):
    arr[i] = arr[i] / 100
# print(arr)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
totalPerc = 0

def dfs(x, y, perc, cnt, visited):
    global totalPerc

    if cnt == k:
        totalPerc += perc
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (nx, ny) not in visited:
            visited.append((nx, ny))
            dfs(nx, ny, perc * arr[i], cnt + 1, visited)
            visited.pop()


dfs(0, 0, 1, 0, [(0, 0)])
print(totalPerc)