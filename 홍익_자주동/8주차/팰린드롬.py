# BOJ 10942

import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
dp = [[0] * n for _ in range(n)]


for i in range(n):
    dp[i][i] = 1
    for j in range(n):
        s = i-j
        e = i - 1 + j
        if 0<=s<n and 0<= e < n:
            if arr[s] != arr[e]:
                dp[s][e] = 0
                break
            dp[s][e] = 1

    for j in range(n):
        s = i - j
        e = i + j
        if 0 <= s < n and 0 <= e < n:
            if arr[s] != arr[e]:
                dp[s][e] = 0
                break
            dp[s][e] = 1

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(dp[a-1][b-1])





