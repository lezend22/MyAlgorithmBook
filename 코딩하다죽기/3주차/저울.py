import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

e = min(arr)
E = sum(arr)
arr.sort()
for i in range(e, E):
    rem = i
    # print(rem)
    for j in range(n-1, -1, -1):
        p = arr[j]
        if rem in arr[:j]:
            rem = 0
            break
        if p <= rem:
            # print("H", p)
            rem -= p
        # print(rem)
        if rem == 0:
            break
    # print("this", rem)
    if rem:
        print(i)
        break