import sys
from collections import deque
sys.setrecursionlimit(111111)

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    h1, h2 = map(int, sys.stdin.readline().split())
    conv = []
    visited = []
    flag = False
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        conv.append((a, b))
    e1, e2 = map(int, sys.stdin.readline().split())
    conv.append((e1, e2))

    queue = deque()
    queue.append((h1, h2))
    visited.append((h1, h2))
    while queue:
        x, y = queue.popleft()
        # print(x, y)
        if x == e1 and y == e2:
            flag = True
            break
        for a, b in conv:

            if (a, b) not in visited:
                k = abs(x-a) + abs(y-b)
                # print(k)
                if k <= 1000:
                    queue.append((a, b))
                    visited.append((a, b))
        # print(queue)

    if flag:
        print("happy")
    else:
        print("sad")
