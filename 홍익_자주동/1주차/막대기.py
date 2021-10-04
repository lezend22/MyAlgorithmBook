import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    m = int(sys.stdin.readline())
    arr.append(m)

pivot = arr[n-1]
count = 1
for i in reversed(range(n-1)):
    if arr[i] <= pivot:
        continue
    else:
        count += 1
        pivot = arr[i]


print(count)
