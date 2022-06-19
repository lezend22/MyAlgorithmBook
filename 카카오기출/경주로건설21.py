from collections import deque

arr = []
INF = 1e9
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def findPath():
    block = [[[INF for _ in range(len(arr))] for _ in range(len(arr))] for _ in range(4)]
    queue = deque()
    queue.append((0, 0, 0, 0))

    while queue:
        x, y, d, cost = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(arr) and 0 <= ny < len(arr) and arr[nx][ny] == 0:
                if nx == 0 and ny == 0:
                    continue

                tempCost = cost
                if x == 0 and y == 0:
                    tempCost += 100
                else:
                    if d != i:
                        tempCost += 600
                    else:
                        tempCost += 100
                # print(i, nx, ny)

                if block[i][nx][ny] > tempCost:
                    block[i][nx][ny] = tempCost
                    queue.append((nx, ny, i, tempCost))

    # print(block)
    ret = INF
    for b in block:
        ret = min(ret, b[-1][-1])

    return ret

def solution(board):
    global arr
    arr = board
    answer = findPath()
    return answer

print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))