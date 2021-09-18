import sys
from collections import deque

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
k = int(sys.stdin.readline())

queue = deque()
visited = []
count = 0

for i in range(len(arr)):
    if arr[i] == -1:
        queue.append(i)
        visited.append(i)

while queue:
    v = queue.popleft()

    if v == k:
        visited.remove(v)
        arr[v] = -2
        continue

    for i in range(len(arr)):
        if arr[i] == v:
            queue.append(i)
            visited.append(i)

for j in visited:
    if j not in arr:
        count+=1


print(count)