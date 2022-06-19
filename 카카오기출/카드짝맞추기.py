from collections import deque, defaultdict
from itertools import permutations
arr = []
Min = 1e9
def control_move(x, y, dx, dy):
    cnt = 0
    while True:
        nx = x + dx
        ny = y + dy
        cnt += 1
        if nx == 0 or nx == 3 or ny == 0 or ny == 3:
            return nx, ny, cnt
        else:
            if arr[nx][ny] != 0:
                return nx, ny, cnt
        x, y = nx, ny

def bfs(s, e):
    Min = 1e9

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    a, b = s
    fx, fy = e
    queue = deque()
    queue.append((a, b, 0))
    visited = [[False] * 4 for _ in range(4)]
    visited[a][b] = True

    while queue:
        x, y, c = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 4 and 0 <= ny < 4 and arr[nx][ny] == 0 and not visited[nx][ny]:
                if nx == fx and ny == fy:
                    return c + 1 #include enter
                queue.append((nx, ny, c+1))
                visited[nx][ny] = True

            nx, ny, c2, = control_move(x, y, dx[i], dy[i])
            if nx == fx and ny == fy:
                return c + c2 + 1
            queue.append((nx, ny, c + c2))
            visited[nx][ny] = True


def findDist(sx, sy, cnt, order, dist):
    global Min

    if cnt == len(order) - 1:
        Min = min(Min, dist)
        return

    f1x, f1y = order[cnt][0]
    f2x, f2y = order[cnt][1]
    d1 = bfs((sx, sy), (f1x, f1y))
    d2 = bfs((sx, sy), (f2x, f2y))
    findDist(f1x, f1y, cnt + 1, order, dist + d1)
    findDist(f2x, f2y, cnt + 1, order, dist + d2)



def solution(board, r, c):
    global arr
    arr = board
    dic = defaultdict(list)
    for i in range(4):
        for j in range(4):
            if arr[i][j] != 0:
                dic[arr[i][j]].append((i, j))

    existChar = list(dic.keys())
    p = list(permutations(existChar))
    for li in p:
        findDist(r, c, 0, li, 0)

    answer = 0
    return answer


solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0)