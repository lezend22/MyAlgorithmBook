import sys
from collections import deque

n = int(sys.stdin.readline())
parent = list(map(int, sys.stdin.readline().split()))
delNode = int(sys.stdin.readline())

queue = deque()
visited = []
for i in range(len(parent)):

    if parent[i] == -1:
        queue.append(i)
        visited.append(i)

while queue:
    popleft = queue.popleft()
    if popleft == delNode:
        visited.remove(popleft)
        parent[popleft] = -2
        continue

    for i in range(len(parent)):
        if parent[i] == popleft:
            queue.append(i)
            visited.append(i)

# print(visited)
# print(parent)
count = 0
for j in visited:
    if j not in parent:
        count += 1

print(count)