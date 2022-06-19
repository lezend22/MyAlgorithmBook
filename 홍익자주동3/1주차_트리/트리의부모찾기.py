import sys

n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
parent = [0] * (n+1)

def dfs(root):

    # print("dfs", root)
    visited = {-1}
    stack = []
    stack.append(root)
    visited.add(root)
    while stack:
        pop = stack.pop()
        for node in graph[pop]:
            if node not in visited:
                stack.append(node)
                parent[node] = pop
                visited.add(node)
    return

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
for i in range(2, n+1):
    print(parent[i])



