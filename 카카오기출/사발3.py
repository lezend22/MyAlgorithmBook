from copy import deepcopy

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def solution(board, aloc, bloc):
    tempBoard = deepcopy(board)
    taloc, tbloc = aloc, bloc
    r = len(board)
    c = len(board[0])


    def check_distance(curr, target):
        x, y = curr
        tx, ty = target
        l_ = abs(x - tx) + abs(y - ty)
        return l_

    def move(curr, target, arr):
        x, y = curr
        pivot = 1e9
        rx, ry = -1, -1
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < r and 0 <= ny < c and arr[nx][ny]:
                dist = check_distance([nx, ny], target)
                if dist < pivot:
                    pivot = dist
                    rx, ry = nx, ny

        arr[x][y] = 0
        return [rx, ry]

    def check(aloc, bloc, arr):
        # awin, bwin, nobody win = 1, 2, 0
        ax, ay = aloc
        bx, by = bloc
        if arr[ax][ay] == 0:
            return 2
        elif arr[bx][by] == 0:
            return 1

        return 0

    def move_check(aloc, bloc):
        print(aloc, bloc)
        if aloc == [-1, -1]:
            return 2
        elif bloc == [-1, -1]:
            return 1

        return 0

    def run(curr, target, arr):
        x, y = curr
        pivot = 0
        rx, ry = -1, -1
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < r and 0 <= ny < c and arr[nx][ny]:
                dist = check_distance([nx, ny], target)
                if dist >= pivot:
                    pivot = dist
                    rx, ry = nx, ny

        arr[x][y] = 0
        return [rx, ry]

    ATurn = True
    init = True
    bRun = False
    cnt = 0
    while True:

        print(taloc, tbloc, tempBoard)
        check_ = check(taloc, tbloc, tempBoard)
        if check_:
            if check_ == 2:
                # b가 이기면 그대로 반환
                answer = cnt
                return answer
            else:
                if not init:
                    answer = cnt
                    return answer
                # a가 이기면 b 도망가야함
                print("Init", cnt)
                cnt = 0
                taloc, tbloc = aloc, bloc
                ATurn = True
                bRun = True
                init = False
                tempBoard = board
                continue

        # 거짓이면 break 이동거리 반환
        # move
        if ATurn:
            taloc = move(taloc, tbloc, tempBoard)
            ATurn = False
        else:
            if not bRun:
                tbloc = move(tbloc, taloc, tempBoard)
            else:
                tbloc = run(tbloc, taloc, tempBoard)
            ATurn = True

        if move_check(taloc, tbloc):
            answer = cnt
            return answer

        cnt += 1


print(solution([[1, 1, 1, 1, 1]], [0, 0], [0, 4]))