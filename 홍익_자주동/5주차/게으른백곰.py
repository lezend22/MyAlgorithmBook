import sys

n, k = map(int, sys.stdin.readline().split())
arr = [0] * 1000001
ice = []
result = 0
for _ in range(n):
    g, x = map(int, sys.stdin.readline().split())
    ice.append(x)
    arr[x] = g

ice.sort()
left = ice[0]
right = ice[-1]
end = left
for i in range(left, right+1):
    total = 0
    start = i
    while end <= right and (end - start) <= 2*k:
        if arr[end]:
            total += arr[end]
        end += 1
    result = max(result, total)
print(result)