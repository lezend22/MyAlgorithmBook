# str문자열 형식으로받아와서 문자열 덧셈으로 편하게 구현
# dfs 재귀함수를 이용 완전탐색
# 재귀함수 구조를 잘 파악
# 재귀 탈출 조건 주의하여 짜야함
import sys

arr = [list(map(str, sys.stdin.readline().split())) for _ in range(5)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
total = []

def dfs(x, y, num):
    if len(num) == 6:
        if num not in total:
            total.append(num)
            # print("append total ", num)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx <= 4 and ny >= 0 and ny <= 4:
            # print('(',nx, ny,')', arr[nx][ny])
            dfs(nx, ny, num+arr[nx][ny])
            # print(num)

for i in range(5):
    for j in range(5):
        dfs(i, j, arr[i][j])

print(len(total))