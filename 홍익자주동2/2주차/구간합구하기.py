import sys

n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for _ in range(m):

    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1

    for i in range(x1, x2+1):
        for j in range(y1, y2+1):


