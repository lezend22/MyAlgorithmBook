import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()
max = arr[n-1]

for i in range(len(arr)-1):
    max += (arr[i] / 2)


print(round(max, 2))

### so ez

