import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
travel = list(map(int, sys.stdin.readline().split()))

def dfs(n, k):

    queue = deque()
    queue.append(n)
    visited = []
    while queue:

        popleft = queue.popleft()
        if popleft == k:
            return True

        for i in range(n):
            if graph[popleft][i] == 1:
                queue.append(i)
                visited.append(i)

    return False

for i in range(m-1):
    print(travel[i], travel[i+1])
    print(dfs(travel[i]-1, travel[i+1]-1))