import sys
from collections import deque, defaultdict
from itertools import combinations

n = int(sys.stdin.readline())
population = [int(x) for x in sys.stdin.readline().split()]
graph = [[] for _ in range(n)]
# g = defaultdict(list)
result = sys.maxsize

for i in range(n):
    arr = list(map(int, sys.stdin.readline().split()))
    for j in range(arr[0]):
        graph[i].append(arr[j+1] - 1)


# for i in range(n):
#     _input = [int(x) for x in sys.stdin.readline().split()]
#     for j in range(ssg, _input[0]+ssg):
#         g[i].append(_input[j]-ssg)
#
# print(g)

def bfs(combi):
    start = combi[0]
    q = deque([start])
    visited = set([start])
    _sum = 0
    while q:
        popleft = q.popleft()
        _sum += population[popleft]
        for i in graph[popleft]:
            if i not in visited and i in combi:
                q.append(i)
                visited.add(i)

    return _sum, len(visited)

for i in range(1, n//2 + 1):
    combis = list(combinations(range(n), i))
    for combi in combis:
        sum1, v1 = bfs(combi)
        sum2, v2 = bfs([i for i in range(n) if i not in combi])
        if (v1 + v2) == n:
            result = min(result, abs(sum1 - sum2))

if result == sys.maxsize:
    print(-1)
else:
    print(result)