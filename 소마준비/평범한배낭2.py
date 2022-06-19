import sys

n, m = map(int, sys.stdin.readline().split())

v, c = [0], [0]
t = 0
for _ in range(n):
    a, b, d = map(int, sys.stdin.readline().split())

    idx = 1
    while d > 0:

        tmp = min(idx, d)
        v.append(a * tmp)
        c.append(b * tmp)

        d -= idx
        idx = 2 * idx

# print(v)
# print(c)
dp = [0] * (m+1)
for i in range(1, len(v)):
        for j in range(m, 0, -1):
            if j-v[i] >= 0:
                dp[j] = max(dp[j], dp[j-v[i]]+ c[i])

print(dp[m])