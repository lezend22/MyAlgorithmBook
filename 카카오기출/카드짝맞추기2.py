from collections import defaultdict, deque
from copy import deepcopy
from itertools import permutations

def move_cost2(board, start, target):
    r, c = start
    if (r, c) == target: return 0
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]

    queue = deque()
    visited = []
    queue.append((r, c, 0))
    visited.append((r, c))

    while queue:
        x, y, d, = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            cx, cy = x, y

            while True:
                cx, cy = cx + dx[i], cy + dy[i]
                if 0 <= cx < 4 and 0 <= cy < 4 and board[cx][cy]:
                    break
                elif not (0 <= cx < 4 and 0 <= cy < 4):
                    cx = cx - dx[i]
                    cy = cy - dy[i]
                    break

            if (nx, ny) == target or (cx, cy) == target:
                return d + 1

            if 0 <= nx < 4 and 0 <= ny < 4 and (nx, ny) not in visited:
                queue.append((nx, ny, d + 1))
                visited.append((nx, ny))
            if (cx, cy) not in visited:
                queue.append((cx, cy, d + 1))
                visited.append((cx, cy))


def move_cost(board, start, end):   # 조작 횟수 Count
    if start==end: return 0
    queue, visit = deque([[start[0], start[1], 0]]), {start}
    while queue:                    # BFS
        x, y, c = queue.popleft()
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx, ny = x+dx, y+dy     # Normal move
            cx, cy = x, y
            while True:             # Ctrl + move
                cx, cy = cx+dx, cy+dy
                if not (0 <= cx <= 3 and 0 <= cy <= 3):
                    cx, cy = cx-dx, cy-dy
                    break
                elif board[cx][cy] != 0:
                    break

            if (nx, ny) == end or (cx, cy) == end:  # 도착 최단 경로
                return c+1

            if (0 <= nx <= 3 and 0 <= ny <= 3) and (nx, ny) not in visit:
                queue.append((nx, ny, c+1))
                visit.add((nx, ny))
            if (cx, cy) not in visit:
                queue.append((cx, cy, c+1))
                visit.add((cx, cy))



def getPath(board, dic, start, case, cost):
    if len(case) == 0:
        return cost

    # 1, 2, 3 case
    # 2, 3
    # 3
    # ()
    # r,c
    # dic[1] = [(0, 0), (1, 3)]
    # f1 = start -> 어피치의 1번 장소로 가기까지 cost + 1번장소에서 -> 2번 장소로까지 가는 cost + 2 (enter)
    # (0, 0) (1, 3) 2가지
    f1 = move_cost2(board, start, dic[case[0]][0]) + move_cost2(board, dic[case[0]][0], dic[case[0]][1]) + 2
    f2 = move_cost2(board, start, dic[case[0]][1]) + move_cost2(board, dic[case[0]][1], dic[case[0]][0]) + 2
    print("###", f1, f2)
    pos = dic[case[0]]
    temp = deepcopy(board)
    for a, b in pos:
        temp[a][b] = 0
    if f1 < f2:
        return getPath(temp, dic, dic[case[0]][1], case[1:], cost + f1)
    else:
        return getPath(temp, dic, dic[case[0]][0], case[1:], cost + f2)

def solution(board, r, c):
    dic = defaultdict(list)
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                dic[board[i][j]].append((i, j))
    answer = 1e9
    for case in permutations(range(1, len(dic)+1), len(dic)):
        print(case)
        answer = min(answer, getPath(board, dic, (r, c), case, 0))

    return answer

print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0))
