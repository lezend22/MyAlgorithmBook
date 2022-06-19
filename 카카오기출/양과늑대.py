from collections import defaultdict

dic = defaultdict(list)
info = []
maxSheep = 0


def findMaxSheep(start, wolf, sheep, can_go, visited):
    global maxSheep
    start_ = info[start]
    if visited[start]:
        return
    visited[start] = True

    if start_ == 1:
        wolf += 1
    else:
        sheep += 1
        maxSheep = max(maxSheep, sheep)
    if sheep == wolf:
        return

    can_go += dic[start]
    for i in can_go:
        next_go = [x for x in can_go if x != i and not visited[x]]
        next_visited = visited[:]
        findMaxSheep(i, wolf, sheep, next_go, next_visited)


def solution(infos, edges):
    global info
    visited = [False] * len(infos)
    for edge in edges:
        a, b = edge
        dic[a].append(b)

    info = infos
    findMaxSheep(0, 0, 0, [], visited)
    return maxSheep

print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
