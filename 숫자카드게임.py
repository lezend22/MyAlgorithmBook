import sys

INF = sys.maxsize
N,M = map(int, sys.stdin.readline().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(arr)
minArr = list()

for i in range(N):
    minNum = INF
    for j in range(M):
        if minNum > arr[i][j]:
            minNum = arr[i][j]
    minArr.append(minNum)

print(minArr)
print(max(minArr))
