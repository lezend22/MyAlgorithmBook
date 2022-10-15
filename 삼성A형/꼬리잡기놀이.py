from collections import deque


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def getPath():

    def bfs(i, j):
        s, e = 0, 0
        cnt = 0
        leng = 1
        path = [(i, j)]
        queue = deque([(i, j)])
        visited = {(i, j)}
        flag = False

        while queue:
            x, y, = queue.popleft()
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                    if not arr[nx][ny]:
                        continue

                    if arr[nx][ny] == 4:
                        path.append((nx, ny))
                        queue.append((nx, ny))
                        visited.add((nx, ny))

                    # 꼬리
                    elif arr[nx][ny] == 3:
                        path.append((nx, ny))
                        queue.append((nx, ny))
                        leng += 1
                        flag = True
                        visited.add((nx, ny))
                        e = cnt

                    elif flag and arr[nx][ny] == 2:
                        path.append((nx, ny))
                        queue.append((nx, ny))
                        visited.add((nx, ny))
                        leng += 1

                    cnt += 1

        return (s, e, leng, 0, path)

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                ret = bfs(i, j)
                teams.append(ret)


def move():

    def check(s, e, leng):
        s = s % leng
        e = e % leng
        return s, e

    for team in teams:
        s, e, leng, flag, path = team

        # 처음 순방향
        if not flag:
            s += 1
            e += 1
            s, e = check(s, e, leng)
            sFind = False
            for i in range(len(path)):
                px, py = path[i]

                if i == s:
                    sFind = True
                    arr[px][py] = 1






n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
teams = []

getPath()
print(teams)

for _ in range(k):

# 움직여

