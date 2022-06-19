import sys
from collections import defaultdict


n = int(sys.stdin.readline())

cnt = defaultdict(int)
r = list(tuple(map(int, sys.stdin.readline().split())) for _ in range(n))
for i in range(n):
    s, e = r[i]
    cnt[s] += 1
    cnt[e] -= 1

# print(cnt)
keys = list(cnt.keys())
keys.sort()
rg = []
current = 0
for i in keys:
    current += cnt[i]
    rg.append(current)

# print(rg)

max_ = max(rg)
idx = rg.index(max(rg))
end = -1
for i in range(idx, len(rg)):
    if rg[i] != max_:
        end = i
        break

print(max_)
print(keys[idx], keys[end])