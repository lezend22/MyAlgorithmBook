import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

answer = [0] * n
pivot = arr[0]
for i in range(1, n):
    if pivot != arr[i]:
        answer[i-1] = i+1
        pivot = arr[i]

p = 0
for i in range(n-1, -1, -1):
    if not p:
        answer[i] = -1
    if answer[i]:
        p = answer[i]
        continue
    if p:
        answer[i] = p

print(answer)

