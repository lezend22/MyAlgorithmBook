import sys

answer = -1
n = int(sys.stdin.readline())
arr = []
texp = 0
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    texp += b
    arr.append((a, b))

arr.sort(key=lambda x:x[0])
cnt = 0
for key, val in arr:
    cnt += val
    if cnt > texp // 2:
        answer = key
        break

print(answer)



