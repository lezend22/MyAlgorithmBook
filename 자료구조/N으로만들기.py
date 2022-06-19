import sys
from collections import deque

num = list(map(int, sys.stdin.readline().rstrip()))
method = []
ans = -1
indexVisited = {-2}

def dfs(curr, idx, path):
    global ans

    if idx < 0 or idx >= len(num) or idx in indexVisited:
        return

    print(path, num)
    if len(path) == len(num):
        if path not in method:
            ans += 1
            method.append(path)

    if idx-1 >= 0:
        print(num[idx-1])
        a1 = curr.appendleft(num[idx - 1])
        path.append(a1)
        dfs(curr, idx - 1, path)
    if idx + len(curr) < len(num):
        print(num[idx + len(curr)])
        curr.append(num[idx + len(curr)])
        temp = curr[:]
        path.append(temp)
        dfs(curr, idx + len(curr), path)



for i in range(len(num)):
    queue = deque()
    queue.append(num[i])
    dfs(queue, i, [queue])

print(ans)