# pypy로 컴파일해서 일단 맞긴했는데 시간복잡도 완전 안좋아
# 모든 0set에서 ssg 3개 뽑는 조합 : 모든 경우의 수
# 모든 경우의수에 대해 전부 감염시킴
# 감염 시킨 후 감염된 칸 2의 개수 전부 count
# 이후 총 개수 - min(감염된칸) - 1의 개수 - 3(추가로 더한 ssg)
import sys
from collections import deque
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
queue = deque()
index = []
result = 0
total = []
one = 0

def loop():
    count = 1
    while queue:
        v = queue.popleft()
        # print(v)
        x, y = v
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m and (nx, ny) not in visited and arr[nx][ny] == 0:
                queue.append((nx, ny))
                visited.append((nx, ny))
                count += 1
    return count

def check(d):
    resultNum = 0
    for r in d:
        a, b = r
        arr[a][b] = 1
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2 and (i, j) not in visited:
                queue.append((i, j))
                visited.append((i, j))
                resultNum += loop()
    for r in d:
        a, b = r
        arr[a][b] = 0
    return resultNum

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            index.append((i, j))
        elif arr[i][j] == 1:
            one += 1
l = list(combinations(index, 3))

for i in l:
    visited = []
    result = check(i)
    total.append(result)

r1 = (m*n) - one - min(total) - 3
print(r1)
