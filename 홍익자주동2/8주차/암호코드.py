import sys

arr = list(map(int, list(sys.stdin.readline().rstrip())))
dp = [0] * (len(arr)+1)
dp[0] = 1
dp[1] = 1
if arr[0] == 0:
    print(0)
    exit(0)

arr = [0] + arr
for i in range(2, len(arr)):
    if 0 < arr[i] < 10:
        dp[i] += dp[i-1]
    temp = arr[i-1] * 10 + arr[i]
    # print(temp)
    if 10 <= temp <= 26:
        dp[i] += dp[i-2]

print(dp[len(arr)-1] % 1000000)