import sys
from collections import deque

n, c = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
edges = []
for _ in range(m):
    a, b, e = map(int, sys.stdin.readline().split())
    edges.append((b, a, e))

edges.sort()
queue = deque(edges)
arr = [c] * (n + 1)

def getBox():
    ans = 0

    while queue:
        b, a, cost = queue.popleft()
        min_ = min(arr[a:b])
        if min_ < cost:
            for i in range(a, b):
                arr[i] -= min_
            ans += min_
        else:
            for i in range(a, b):
                arr[i] -= cost
            ans += cost

    return ans

print(getBox())