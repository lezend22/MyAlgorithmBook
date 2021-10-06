# deque으로 간단하게 풀수있음
# 덱에서 맨 앞 원소보다 크면 appendleft
# else append()

import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline().rstrip().split(" ")

    queue = deque(arr[0])
    for i in range(1, len(arr)):
        if arr[i] <= queue[0]:
            queue.appendleft(arr[i])
        else:
            queue.append(arr[i])

    print("".join(queue))

