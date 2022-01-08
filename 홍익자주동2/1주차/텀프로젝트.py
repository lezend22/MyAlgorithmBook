import sys
sys.setrecursionlimit(111111)

t = int(sys.stdin.readline())

for k in range(t):

    n = int(sys.stdin.readline())
    graph = list(map(int, sys.stdin.readline().split()))
    graph = [0] + graph
    visited = [0] * (n+1)
    # print(visited)
    cycle = 0
    def dfs(here):

        global cycle
        traced.append(here)
        visited[here] = 1

        w = graph[here]

        if visited[w] == 1:
            if w in traced:
                cycle += len(traced[traced.index(w):])
            return None
        else:
            dfs(w)

    for i in range(1, n+1):

        if visited[i] == 0:
            traced = []
            dfs(i)

    print(n - cycle)