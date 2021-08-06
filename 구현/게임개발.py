import sys

n, m = map(int, sys.stdin.readline().split())

a, b, d = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
print(arr)
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

direct = [0, 1, 2, 3]
visted = list()

def turnLeft(d):
    d = d-1
    if d == -1:
        d = 3
    return d

##start
visted.append((a,b))
turnCount = 0
while True:
    if turnCount == 4:
        turnLeft(d)
        turnLeft(d)
        nx = a + dx[d]
        ny = b + dy[d]
        if arr[nx][ny] == 1:
            break
        else:
            turnCount = 0
            continue

    d = turnLeft(d)
    nx = a + dx[d]
    ny = b + dy[d]
    if nx >= 0 and nx <= m and ny >= 0 and ny <= n and arr[nx][ny] == 0 and (nx,ny) not in visted:
        a = nx
        b = ny
        visted.append((a,b))
    turnCount +=1

print(visted)
print(len(visted))
