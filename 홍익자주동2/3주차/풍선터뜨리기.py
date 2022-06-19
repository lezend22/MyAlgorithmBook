import sys

n = int(sys.stdin.readline())
queue = list(map(int, sys.stdin.readline().split()))
visited = []
pk = 0

while True:

    print(pk+1, end=' ')

    p = queue[pk]
    visited.append(pk)
    if len(visited) == n:
        break

    if p > 0:
        cnt = 0
        while True:
            if cnt == p:
                break
            pk += 1

            if pk >= 0:
                pk = pk % n
            else:
                pk = pk + n

            if pk not in visited:
                cnt += 1

    else:
        cnt = 0
        while True:
            if cnt == abs(p):
                break
            pk -= 1

            if pk >= 0:
                pk = pk % n
            else:
                pk = pk + n

            if pk not in visited:
                cnt += 1



