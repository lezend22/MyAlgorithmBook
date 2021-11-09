import sys

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
eat, count = 0, 0
check = True

while check:
    for i in range(n):
        if i+1 > k:
            if arr[i] > arr[i - k]:
                eat += (arr[i] - arr[i-k])
                arr[i] = arr[i-k]
                l = sorted(arr)
                count += 1
                if arr == l:
                    check = False
                arr = l
            else:
                sorted1 = sorted(arr)
                if arr == sorted1:
                    check = False
print(eat, count)


