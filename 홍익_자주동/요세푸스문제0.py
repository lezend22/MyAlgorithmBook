import sys

n, k = map(int, sys.stdin.readline().split())
arr = list(range(1, n+1))

result = []

# list로 쇼부
while arr:
    r = k
    if len(arr) == 1:
        result.extend(arr)
        break
    if len(arr) < k:
        r = k % len(arr)
        if r == 0:
            result.append(arr[r - 1])
            arr = arr[:r-1]
            continue

    result.append(arr[r-1])
    arr = arr[r:] + arr[:r-1]


# Output
print("<", end='')
for i in result:
    if i == result[-1]:
        print(i, end='')
    else:
        print(i, end=', ')
print(">", end='')