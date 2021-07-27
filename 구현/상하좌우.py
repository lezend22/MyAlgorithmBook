import sys

n = int(sys.stdin.readline().rstrip())
plans = sys.stdin.readline().split()

x, y = 1, 1

movType = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for plan in plans:
    for i in range(len(movType)):
        if plan == movType[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx<1 or ny<1 or nx>n or ny>n:
        continue

    x, y = nx, ny

print(x,y)


