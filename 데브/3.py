dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
plant = []

def check_(pos, board, check):
    x, y = pos
    cnt = 0
    path = []
    for d in range(8):
        nx = x + dx[d]
        ny = y + dy[d]
        if (nx, ny) not in plant and 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == '.':
            cnt += 1
            check[x][y].append((nx, ny))
            path.append((nx, ny))

    # 반드시 있음
    if cnt == board[x][y]:
        for a, b in path:
            plant.append((a, b))
            board[a][b] = 'S'






def solution(board):
    check = [[[] for _ in range(len(board[0]))] for _ in range(len(board))]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if arr[i][j]:



    answer = []
    return answer

solution([".1...2", "111.3."])