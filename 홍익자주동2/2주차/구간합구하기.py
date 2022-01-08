import sys

n, m = map(int, sys.stdin.readline().split())
arr = [[0] * (n+1)] + [[0] + list(map(int, sys.stdin.readline().split())) for _ in range(n)]
mem = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1 and j == 1:
            mem[i][j] = arr[i][j]
        else:
            if i == 1:
                mem[i][j] = mem[i][j-1] + arr[i][j]
            elif j == 1:
                mem[i][j] = mem[i-1][j] + arr[i][j]

            else:
                mem[i][j] = mem[i-1][j] + mem[i][j-1] + arr[i][j] - mem[i-1][j-1]

for i in range(1, m+1):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    result = mem[x2][y2] - mem[x1-1][y2] - mem[x2][y1-1] + mem[x1-1][y1-1]
    print(result)
