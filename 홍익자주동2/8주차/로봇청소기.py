import sys

def dfs(i, j, dir):
    # print("#####")
    d = dir
    # print("dfs start", i, j)
    if (i, j) not in visited:
        visited.append((i, j))
    px, py = i, j

    #왼쪽으로 회전
    i = 0
    while i < 4:
        d = d - 1
        if d < 0:
            d = 4 + d
        nx = px + dx[d]
        ny = py + dy[d]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != 1 and (nx, ny) not in visited:
            return dfs(nx, ny, d)
        else:
            i += 1

    return px, py, d

def backward(i, j, d):
    px, py = i, j
    # print(px, py, "second in")
    nd = d - 2
    if nd < 0:
        nd = 4 + nd
    nx = px + dx[nd]
    ny = py + dy[nd]
    if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != 1:
        # print("here2", nx, ny)
        px, py, d = dfs(nx, ny, d)
        backward(px, py, d)

    return

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    r, c, d = map(int, sys.stdin.readline().split())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    # 0 : 북쪽 / ssg: 동쪽 / 2: 남쪽 / 3:서쪽
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    visited = []
    px, py, d = dfs(r, c, d)
    # print(px, py, d)
    backward(px, py, d)
    # print(visited)
    print(len(visited))
