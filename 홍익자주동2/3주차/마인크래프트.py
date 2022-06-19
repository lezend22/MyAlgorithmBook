import sys

n, m, b = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


minh = min(arr)
maxh = max(arr)

for h in range(minh, maxh):
