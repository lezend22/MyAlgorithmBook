import sys
from collections import deque

queue = deque()
count = 0
n,d,k,c = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(n)]
arr += arr[:k-1]
counter = [0 for _ in range(d+1)]
result = 0
window = deque()
for i, v in enumerate(arr):
    window.append(v)
    counter[v] += 1

    if counter[v] == 1:
        count += 1

    if i < k-1:
        continue

    if counter[c] == 0:
        result = max(result, count + 1)
    else:
        result = max(result, count)

    popleft = window.popleft()
    counter[popleft] -= 1
    if counter[popleft] == 0:
        count -= 1


print(result)