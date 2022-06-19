import sys

n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

max_ = -1
for i in arr:
    m = min(i)
    if max_ < m:
        max_ = m

print(max_)