import sys

a, b = map(int, sys.stdin.readline().split())
ret = 0
def dfs(n):
    global ret
    if n > b:
        return
    elif a <= n <= b:
        ret += 1

    dfs(n*10+4)
    dfs(n*10+7)

dfs(4)
dfs(7)

print(ret)