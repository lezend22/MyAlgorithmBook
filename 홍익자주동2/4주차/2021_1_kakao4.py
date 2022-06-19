from collections import deque
import sys

sys.setrecursionlimit(1000)
answer = 1e9
def reverse(graph, n):

    print("reverse")
    tmp = []
    for i in range(1, len(graph)):
        for a, b in graph[i]:
            if a == n:
                tmp.append((i, b))
                graph[i].remove((a, b))

    for a1, b1 in graph[n]:
        graph[a1].append((n, b1))
    graph[n] = tmp

    print(graph)
    return graph

def dfs(n, graph, traps, end, size):
    global answer
    print("현재 node", n)

    if n == end:
        print("get to finish")
        answer = min(size, answer)
        return

    tmp = 0
    if n in traps:
        tmp = reverse(graph, n)
    else:
        tmp = graph

    for a, b in graph[n]:

        dfs(a, tmp, traps, end, size+b)
    print("fail")


def solution(n, start, end, roads, traps):
    global answer
    graph = [[] for _ in range(n+1)]
    for road in roads:
        a, b, c = map(int, road)
        graph[a].append((b, c))
    print(graph)

    dfs(start, graph, traps, end, 0)

    return answer

print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))