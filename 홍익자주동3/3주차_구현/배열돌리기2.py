import sys

n, m, r = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def solution(p, n, m):

    idx = 0
    for i in range(p, p+m-1):
        row[(idx-r) % length] = arr[p][i]
        idx += 1
    for i in range(p, p+n-1):
        row[(idx-r) % length] = arr[i][p+m-1]
        idx += 1
    for i in range(p + m-1, p, -1):
        row[(idx-r) % length] = arr[p+n-1][i]
        idx += 1
    for i in range(p + n-1, p, -1):
        row[(idx-r) % length] = arr[i][p]
        idx += 1

    # print(row)
    idx = 0
    for i in range(p, p+m-1):
        arr[p][i] = row[idx]
        idx += 1
    for i in range(p, p+n-1):
        arr[i][p+m-1] = row[idx]
        idx += 1
    for i in range(p + m -1, p, -1):
        arr[p+n-1][i] = row[idx]
        idx += 1
    for i in range(p + n - 1, p, -1):
        arr[i][p] = row[idx]
        idx += 1



if __name__ == '__main__':
    depth = min(n, m) // 2
    p = 0
    for _ in range(depth):
        length = (n - 1) * 2 + (m - 1) * 2
        row = [-1] * (length)
        solution(p, n, m)
        p += 1
        n -= 2
        m -= 2
    for i in arr:
        print(*i)