import sys
from collections import deque

chain = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]
k = int(sys.stdin.readline())

chain_status = [0, 0, 0, 0]
status = [(6,2), (5, 1), (4, 0), (3, 7), (2, 6), (1, 5), (0, 4), (7,3)]
point = [False] * 3
print(chain)
t, dir = map(int,sys.stdin.readline().split())
if dir == 1:
    dir = True
else:
    dir = False

for i in range(3):
    a, b = 999, 999
    if i == 0:
        a = status[chain_status[0]][1]
        b = status[chain_status[1]][0]

    elif i == 1:
        a = status[chain_status[1]][1]
        b = status[chain_status[2]][0]
    elif i == 2:
        a = status[chain_status[2]][1]
        b = status[chain_status[3]][0]
    if chain[i][a] == chain[i][b]:
        point[i] = True

queue = deque()
queue.append(t)
visited = []
move = []
print(point)
print(queue)
while queue:
    popleft = queue.popleft()
    if popleft == 1:
        print(point)
        if point[0] and 2 not in visited:
            queue.append(2)
            visited.append(2)
            move.append((2, not dir))
    elif popleft == 2:
        if point[0] and 1 not in visited:
            queue.append(1)
            visited.append(1)
            move.append((1, not dir))
        elif point[1] and 3 not in visited:
            queue.append(3)
            visited.append(3)
            move.append((3, not dir))
    elif popleft == 3:
        if point[1] and 2 not in visited:
            queue.append(2)
            visited.append(2)
            move.append((2, not dir))
        elif point[2] and 4 not in visited:
            queue.append(4)
            visited.append(4)
            move.append((4, not dir))
    elif popleft == 4:
        if point[2] and 3 not in visited:
            queue.append(3)
            visited.append(3)
            move.append((3, not dir))

print(move)








