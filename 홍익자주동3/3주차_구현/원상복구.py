import sys

n, m = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))
d = list(map(int, sys.stdin.readline().split()))

s = [-1] + s
d = [-1] + d

def rollback(s):

    p = [-1] * (n+1)
    for i in range(1, n+1):
        p[d[i]] = s[i]
    # print(p)
    return p

def solution(n, m, s ,d):

    for _ in range(m):
        s = rollback(s)

    ans = s[1:]
    return ans
print(*solution(n, m, s, d))