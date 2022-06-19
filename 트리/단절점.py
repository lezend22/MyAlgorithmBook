import sys
sys.setrecursionlimit(100000)

def dfs(curr, isroot):
    # print("curr", curr)
    global cnt
    child = 0
    cnt += 1
    discover[curr] = cnt
    ret = discover[curr]
    # print(ret)

    for next in graph[curr]:

        if discover[next] == 0:
            child += 1
            mindisc = dfs(next, 0)
            if not isroot and mindisc >= discover[curr]:
                cut[curr] = 1
            ret = min(mindisc, ret)
        else:
            ret = min(ret, discover[next])

    # print(ret)
    if isroot and child > 1:
        # print("isroot", curr, child)
        cut[curr] = 1

    return ret


if __name__ == '__main__':

    v, e = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(v + 1)]
    discover = [0] * (v + 1)
    cut = [0] * (v + 1)
    # print(graph, discover, cut)

    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    cnt = 0
    for i in range(1, v+1):
        # print(discover[i])
        if discover[i] == 0:
            dfs(i, 1)

    print(sum(cut))
    for j in range(1, v+1):
        if cut[j] == 1:
            print(j, end=" ")