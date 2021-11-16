# dfs, bfs둘다 시간초과
# DP로 푸는데, 갔던데 체크 안하면 시간초과...
# n^2으로도 풀어도 괜찮음, 100개밖에안되니까
# 근데 n^2이 안될경우, 재귀로 가야되는데 갔던데 다시 안가도록 체크해야함
# -1로 초기화 후 간곳만 0으로 바꿔서, 0을 더해도 return값에는 문제없도록
import sys

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
d = [[-1] * n for _ in range(n)]
d1 = [[0] * n for _ in range(n)]



# def chain(x, y):
#     if x == n-1 and y == n-1:
#         return 1
#
#     nc = arr[x][y]
#     if d[x][y] == -1:
#         d[x][y] = 0
#         x1, y1 = x + nc, y
#         x2, y2 = x, y + nc
#         if 0 <= x1 < n and 0 <= y1 < n:
#             d[x][y] += chain(x1, y1)
#         if 0 <= x2 < n and 0 <= y2 < n:
#             d[x][y] += chain(x2, y2)
#     return d[x][y]
#
#
# i = chain(0, 0)
# print(i)
