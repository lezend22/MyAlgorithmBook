import sys

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, m = 0, 0

def around(board, x, y):

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny]:
            return True

    return False

def dfs(board, x1, y1, x2, y2):

    min_ = 1e9
    max_ = -1

    if not around(board, x1, x2):
        ## 갈때없음 -> 짐
        return False, 0

    if x1 == x2 and y1 == y2:
        ## 이김 -> 미리 하나 추가
        print("here")
        print(x1, y1, x2, y2)
        return True, 1

    win = False
    for d in range(4):

        nx = x1 + dx[d]
        ny = y1 + dy[d]

        if not (0 <= nx < n and 0 <= ny < m and board[nx][ny]):
            continue
        board[x1][y1] = 0
        flag, cost = dfs(board, x2, y2, nx, ny)
        board[x1][y1] = 1

        if not flag:
            win = True
            min_ = min(min_, cost + 1)

        elif not win:
            print(max_)
            max_ = max(max_, cost + 1)

    if win:
        return True, min_
    else:
        return False, max_


def solution(board, aloc, bloc):
    global n, m
    n, m = len(board), len(board[0])
    flag, ret = dfs(board, aloc[0], aloc[1], bloc[0], bloc[1])
    return ret

print(solution([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [1, 0], [1, 2]))