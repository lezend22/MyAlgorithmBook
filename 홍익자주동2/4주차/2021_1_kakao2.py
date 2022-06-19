from collections import deque

def func(arr, i, j):
    visited = []
    queue = deque()
    queue.append((i, j, 0))
    visited.append((i, j))
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    while queue:
        x, y, tmp = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and tmp < 2 and arr[nx][ny] != 'X' and (nx, ny) not in visited:
                if arr[nx][ny] != 'P':
                    queue.append((nx, ny, tmp+1))
                    visited.append((nx, ny))
                elif arr[nx][ny] == 'P':
                    # print(nx, ny)
                    return False

    return True

def solution(places):
    answer = []
    for place in places:

        arr = []
        for i in place:
            arr.append(i)

        flag = False
        for i in range(5):
            for j in range(5):
                if arr[i][j] == 'P':
                    if func(arr, i, j):
                        continue
                    else:
                        answer.append(0)
                        flag = True
                        break
            if flag:
                break
        if not flag:
            answer.append(1)





    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
