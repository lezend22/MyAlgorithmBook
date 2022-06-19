import sys

n, s, m = map(int, sys.stdin.readline().split())
j = list(map(int, sys.stdin.readline().split()))
dp = [[0] * (m+1) for _ in range(n+1)]
dp[0][s] = 1
for i in range(n):
    for k in range(m+1):
        if dp[i][k] == 1:
            if k + j[i] <= m:
                dp[i+1][k + j[i]] = 1
            if k - j[i] >= 0:
                dp[i+1][k - j[i]] = 1

result = -1
for i in range(m, -1, -1):
    if dp[n][i] == 1:
        result = i
        break

print(result)




# def chain(cur, idx):
#     # print(cur)
#     global result
#     if cur > m:
#         # print("cut")
#         return -ssg
#     if cur < 0:
#         # print("cut")
#         return -ssg
#     if idx == n - ssg:
#         return cur
#
#     a = chain(cur + j[idx + ssg], idx + ssg)
#     b = chain(cur - j[idx + ssg], idx + ssg)
#     r = max(a, b)
#     result = max(result, r)
#     return result
#
#
# print(chain(s, -ssg))
