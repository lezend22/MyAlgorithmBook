from collections import deque
from typing import List




dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
ddx = [-1, 0, 1, 0]
ddy = [0, 1, 0, -1]

def get_fire(fire, farr, n):
    x, y = fire
    fvisit = [(x, y)]
    queue = []
    for d in range(8):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in fvisit:
            farr[nx][ny] += 1
            fvisit.append((nx, ny))
            queue.append(([nx, ny], 0))

    return farr, queue

def solution(n: int, m: int, fires: List[List[int]], ices: List[List[int]]) -> List[List[int]]:
    farr = [[0] * (n) for _ in range(n)]
    iarr = [[0] * (n) for _ in range(n)]

    queue = deque()
    nqueue = []
    fvisit = []
    ivisit = []
    for fire in fires:
        a, b = fire
        a -= 1
        b -= 1
        queue.append(((a, b), 0))
        fvisit.append((a, b))
        farr[a][b] += 1

    for ice in ices:
        a, b = ice
        a -= 1
        b -= 1

        queue.append(((a, b), 1))
        ivisit.append((a, b))
        iarr[a][b] -= 1

    rem = 0
    flag = False
    for time in range(m):
        if not queue:
            rem = time - 1
            break

        if flag:
            for i in range(n):
                for j in range(n):
                    if farr[i][j]:
                        farr[i][j] += 1
                    if iarr[i][j] != 0:
                        iarr[i][j] -= 1
        flag = True

        while queue:
            [x, y], t = queue.popleft()

            if t == 0:
                for d in range(8):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in fvisit:
                        farr[nx][ny] += 1
                        fvisit.append((nx, ny))
                        nqueue.append(([nx, ny], 0))

            else:
                for d in range(4):
                    nx = x + ddx[d]
                    ny = y + ddy[d]
                    if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in ivisit:
                        iarr[nx][ny] -= 1
                        ivisit.append((nx, ny))
                        nqueue.append(([nx, ny], 1))


        queue = deque(nqueue)
        nqueue = []


    for i in farr:
        print(i)
    print()

    for i in iarr:
        print(i)
    print()

    total = [[0] * (n) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            total[i][j] = farr[i][j] + iarr[i][j]

    return total
    # if not rem:
    #     print("SEX")
    #     return total
    # else:
    #     print("SEX2")
    #     for i in total:
    #         print(i)
    #     print()

        # rem = m - rem


print(solution(5, 3, [[5, 5], [1, 3], [5, 2]], [[1, 5], [3, 2]]))