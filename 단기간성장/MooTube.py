# 맨 처음엔 다익스트라 변형으로 풀려함.
# 시간초과 나서 bfs로 풀음, 역시 시간초과
# pypy로 컴파일시 시간초과안남.

# 놓친점. k 이상일 때만 count하면 되는데 K 이상나오는걸 굳이 탐색할 필요가 없음.
# 따라서 queue에 넣기 전 제외 조건에 k 이상인것은 빼줘야함. 아니면 다돌아버림.
from collections import defaultdict, deque
import sys

n, q = map(int, sys.stdin.readline().split())
graph = defaultdict(list)

def bfs(v, k):

    queue = deque()
    queue.append((v, 1e9))
    visited = [0] * (n + 1)
    visited[v] = 1
    ret = 0

    while queue:
        node, dist, = queue.popleft()
        for nd, d in graph[node]:
            d_ = min(dist, d)
            # 추가 조건
            if not visited[nd] and d_ >= k:
                ret += 1
                queue.append((nd, d_))
                visited[nd] = 1

    return ret


for _ in range(n - 1):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

for _ in range(q):
    k, v = map(int, sys.stdin.readline().split())
    print(bfs(v, k))
