
def rotate(arr):
    ret = []
    for i in range(len(arr)):
        temp = []
        for j in range(len(arr)-1, -1, -1):
            temp.append(arr[j][i])
        ret.append(temp)

    return ret

# def show(arr):
#     for i in arr:
#         print(i)
#     print()


def check(n, m, px, py, key, board):
    ret = True
    # 추가하기
    for i in range(m):
        for j in range(m):
            board[px + i][py + j] += key[i][j]

    # check
    # show(board)
    for i in range(n):
        for j in range(n):
            if board[m + i][m + j] != 1:
                ret = False

    # delete
    for i in range(m):
        for j in range(m):
            board[px + i][py + j] -= key[i][j]


    return ret



def solution(key, lock):

    m = len(key)
    n = len(lock)

    # board 가운데에 lock 할당
    board = [[0] * (2*m + n) for _ in range(2*m + n)]
    for i in range(n):
        for j in range(n):
            board[m + i][m + j] = lock[i][j]

    # rotate하면서 확인
    answer = False
    k = 0
    while k < 4:
        for i in range(1, m + n):
            for j in range(1, m + n):
                if check(n, m, i, j, key, board):
                    answer = True
                    break
            if answer:
                break

        if answer:
            break

        k += 1
        if k == 4:
            break
        key = rotate(key)

    return answer

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))