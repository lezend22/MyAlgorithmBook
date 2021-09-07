import sys

t = int(sys.stdin.readline())
arr = list()
for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    arr.append((n, m))

d = [[0] * 30 for _ in range(30)]


##항상 n <= m
def loop(n, m):
    if n == 1:
        return m

    if m < n:
        return 0

    if d[n][m] != 0:
        return d[n][m]

    for j in range(1, m):
        d[n][m] += loop(n-1, m-j)

    return d[n][m]

for x in arr:
    print(loop(x[0], x[1]))
