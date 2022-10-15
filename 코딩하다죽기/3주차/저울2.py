import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

ret = 0
for i in range(len(arr)):
    if ret + 1 >= arr[i]:
        ret += arr[i]
    else:
        break

print(ret+1)