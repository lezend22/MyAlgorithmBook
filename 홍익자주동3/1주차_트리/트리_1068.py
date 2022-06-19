import sys

# 루트가 첫번째가 아님 착각하지마라 테스트케이스에
def dfs(root):
    global cnt

    if root == delNode:
        return
    if len(graph[root]) == 0:
        # print("cnt UP")
        cnt += 1
    else:
        for node in graph[root]:
            # print(node)
            dfs(node)


n = int(sys.stdin.readline())
parent = list(map(int, sys.stdin.readline().split()))
delNode = int(sys.stdin.readline())

graph = [[] for _ in range(n)]
root = 0
for i in range(n):
    if i == delNode:
        pass
    else:
        if parent[i] == -1:
            root = i
            continue
        graph[parent[i]].append(i)

# print(graph)
# print("root", root)
cnt = 0
dfs(root)

print(cnt)
