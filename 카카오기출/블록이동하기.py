# 다 못풀었음
# rotate 함수
# shape, 가로, 세로에 따라 rotate 하는위치 달라짐.
# 지금은 하나만 고려해놓음 가로일때만

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def rotate(d1, d2, d, board):
    n = len(board)
    x1, y1 = d1
    x2, y2 = d2
    flag = False

    nx1, ny1, nx2, ny2 = x1, y1, x2, y2
    if d == 0:
        nx1 = x1 - 1
        ny1 = y1 + 1
        if 0 <= x1 - 1 < n and 0 <= y1 < n and not board[x1-1][y1]:
            flag = True
    elif d == 1:
        nx2 = x2 - 1
        ny2 = y2 - 1
        if 0 <= x2 - 1 < n and 0 <= y2 < n and not board[x2-1][y2]:
            flag = True
    elif d == 2:
        nx1 = x1 + 1
        ny1 = y1 + 1
        if 0 <= x1 + 1 < n and 0 <= y1 < n and not board[x1+1][y1]:
            flag = True
    elif d == 3:
        nx2 = x2 + 1
        ny2 = y2 - 1
        if 0 <= x2 + 1 < n and 0 <= y2 < n and not board[x2+1][y2]:
            flag = True

    if flag:
        return (nx1, ny1, nx2, ny2)
    else:
        return -1


def solution(board):
    answer = 0
    start = ((0, 0), (0, 1))
    queue = []
    heapq.heappush(queue, (0, start))
    n = len(board)

    while queue:
        dist, (d1, d2), = heapq.heappop(queue)
        print(dist, d1, d2)
        if d1 == (n-1, n-1) or d2 == (n-1, n-1):
            answer = dist
            break

        x1, y1 = d1
        x2, y2 = d2
        for d in range(4):
            nx1 = x1 + dx[d]
            ny1 = y1 + dy[d]
            nx2 = x2 + dx[d]
            ny2 = y2 + dy[d]
            if 0 <= nx1 < n and 0 <= ny1 < n and 0 <= nx2 < n and 0 <= ny2 < n:
                if not board[nx1][ny1] and not board[nx2][ny2]:
                    print(nx1, ny1, nx2, ny2)
                    heapq.heappush(queue, (dist + 1, ((nx1, ny1), (nx2, ny2))))

        for d in range(4):
            ret = rotate(d1, d2, d, board)
            if ret == -1:
                continue
            else:
                nx1, ny1, nx2, ny2 = ret
                # if 0 <= nx1 < n and 0 <= ny1 < n and 0 <= nx2 < n and 0 <= ny2 < n:
                if not board[nx1][ny1] and not board[nx2][ny2]:
                    print(nx1, ny1, nx2, ny2)
                    heapq.heappush(queue, (dist + 1, ((nx1, ny1), (nx2, ny2))))

    print(answer)
    return answer

solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]])
