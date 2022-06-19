import sys
from collections import deque

f, s, g, u, d = map(int, sys.stdin.readline().split())
queue = deque()
visited = {s}
queue.append((s, 0))
result = -1

while queue:
    cur, curcnt = queue.popleft()
    # print(cur)
    if cur == g:
        result = curcnt
        break

    if cur + u <= f and cur+u not in visited:
        queue.append((cur+u, curcnt+1))
        visited.add(cur+u)
    if cur - d >= 1 and cur-d not in visited:
        queue.append((cur-d, curcnt+1))
        visited.add(cur-d)

if result == -1:
    print("use the stairs")
else:
    print(result)