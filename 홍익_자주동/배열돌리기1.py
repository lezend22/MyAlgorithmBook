import sys

n, m, r = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


def spin(a, b, c, d):
    temp = arr[a][b]
    for i in range(a + 1, c):
        value = arr[i][b]
        arr[i][b] = temp
        temp = value

    for i in range(b + 1, d):
        value = arr[c - 1][i]
        arr[c - 1][i] = temp
        temp = value

    for i in range(c - 2, a - 1, -1):
        value = arr[i][d - 1]
        arr[i][d - 1] = temp
        temp = value

    for i in range(d - 2, b - 1, -1):
        value = arr[a][i]
        arr[a][i] = temp
        temp = value

    return None


for i in range(r):
    a, b, c, d = 0, 0, n, m
    for j in range(min(n, m) // 2):
        spin(a, b, c, d)
        a += 1
        b += 1
        c -= 1
        d -= 1

for i in arr:
    for j in i:
        print(j, end=' ')
    print()

#
# direct = [0, 1, 2, 3]
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# def move(a, b, n, m):
#
#     while a != n and b != m:
#
#         for i in range(a, n-1):
#             ny = i + dy[3]
#             result[ny][b] = arr[i][b]
#
#         for j in range(b, m-1):
#             nx = j + dx[1]
#             result[n-1][nx] = arr[n-1][j]
#
#         for k in range(a+1, n):
#             ny = k + dy[2]
#             result[ny][m-1] = arr[k][m-1]
#
#         for l in range(b+1, m):
#             nx = l + dx[0]
#             result[a][nx] = arr[a][l]
#
#         a, b = a+1, b+1
#         n, m = n-1, m-1
#
#
#
# for v in range(r):
#     move(0, 0, n, m)
#     arr = [item[:] for item in result]


# for i in result:
#     for j in i:
#         print(j, end=' ')
#     print()
