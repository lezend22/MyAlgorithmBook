from collections import deque

info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]

def dfs(graph, v, visited):

    for i in graph[v]:
        if not visited[i]:
            if dfs(graph, i, visited):
                visited[v] = True




def solution(info, edges):
    graph = [[] for _ in range(len(info))]
    for i in edges:
        a, b = i
        graph[a].append(b)



solution(info, edges)