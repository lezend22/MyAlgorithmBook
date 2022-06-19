from collections import deque

n, m = map(int, input().split())
arr = list(map(int, input().split()))

queue = deque(arr)
print(queue)
queue.rotate()
print(queue)