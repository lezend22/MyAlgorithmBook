import sys
from collections import defaultdict
n = int(sys.stdin.readline())
mosq = []
maxt = 0
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if maxt < b:
        maxt = b
    mosq.append((a, b))

dp = defaultdict(int)

for s, e in mosq:
    dp[s] += 1
    dp[e] -= 1


mmt = max(dp)
flag = 0
start, end = -1, -1
for i in range(len(dp)):
    if flag == 0 and dp[i] == mmt:
        flag = 1
        start = i
    elif flag == 1 and dp[i] != mmt:
        end = i-1
        flag = 3
print(mmt)
print(start, end+1)