

def solution(board, skill):
    answer = 0

    check = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    # print(check)
    for i in range(len(skill)):
        tp, r1, c1, r2, c2, reg = skill[i]
        if tp == 2:
            check[r1][c1] += reg
            check[r1][c2 + 1] -= reg
            check[r2 + 1][c1] -= reg
            check[r2 + 1][c2 + 1] += reg
        else:
            check[r1][c1] -= reg
            check[r1][c2 + 1] += reg
            check[r2 + 1][c1] += reg
            check[r2 + 1][c2 + 1] -= reg

        # print(check)

    #누적합 더하기 , 행먼저
    for i in range(len(check) - 1):
        for j in range(len(check[0]) - 1):
            check[i + 1][j] += check[i][j]

    #열 더하기
    for i in range(len(check[0]) - 1):
        for j in range(len(check) - 1):
            check[i][j + 1] += check[i][j]

    # print(check)

    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += check[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer


print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
               [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))
