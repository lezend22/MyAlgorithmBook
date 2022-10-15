# 재귀를 통한 완전탐색
# 시간초과 이므로 프루닝 필요

def dfs(start, mw, path, summit):
    print(start)
    global intens

    if start in summits_:
        return

    if start in gates_:
        # print("SEX", intens)
        global tot

        if mw <= intens:
            intens = mw

        tot.append([intens, summit])
        return

    for nn in graph[start]:

        node, nw = nn
        if node in path:
            continue
        if nw > intens:
            continue
        else:
            mw_ = max(mw, nw)
            dfs(node, mw_, path + [node], summit)

gates_ = []
summits_ = []
n_ = 0
graph = []
tot = []
intens = 1e9

def solution(n, paths, gates, summits):
    global gates_, summits_, n_, graph
    gates_ = gates
    summits_ = summits
    n_ = n + 1

    graph = [[] for _ in range(n_)]

    for path in paths:
        a, b, c = path
        graph[a].append((b, c))
        graph[b].append((a, c))


    for summit in summits_:
        print("GA", summit)
        for nd in graph[summit]:
            dfs(nd[0], nd[1], [summit], summit)

    tot.sort()
    print(tot)
    # a : intens, b: 봉우리
    a, b = tot[0]
    answer = [b, a]
    return answer

print(solution(5, [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2], [5]))
