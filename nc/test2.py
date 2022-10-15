import sys
sys.setrecursionlimit(100000)
max_ = 0

def dfs(arr, t, n):
    global max_
    max_ = max(max_, max(arr))
    if t == n:
        return

    for i in range(len(arr) - 1):

        p = len(arr) - (i + 1)
        mp = max(p, i + 1)
        tmp = []
        for p_ in range(mp):
            a, b = 0, 0
            a_, b_ = i - p_, i + p_ + 1
            if 0 <= a_ < len(arr):
                a = arr[a_]
            if 0 <= b_ < len(arr):
                b = arr[b_]
            tmp.append(a + b)
        print(tmp, i)
        dfs(tmp, t + 1, n)

def solution(paper, n):

    dfs(paper, 0, n)

solution([7,3,-7,5,-3],2)
print(max_)