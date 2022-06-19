import sys
sys.setrecursionlimit(100000)

class Node():
    def __init__(self, num, left, right):
        self.num = num
        self.left = left
        self.right = right


def inorder(root):
    global end
    if nodes[root].left != -1:
        inorder(nodes[root].left)
    end = nodes[root].num
    if nodes[root].right != -1:
        inorder(nodes[root].right)


def dfs(nd):
    global end, cnt

    if nodes[nd].left != -1:
        dfs(nodes[nd].left)
        cnt += 1

    if nodes[nd].num == end:
        print(cnt)
        exit(0)
    cnt += 1

    if nodes[nd].right != -1:
        dfs(nodes[nd].right)
        cnt += 1



n = int(sys.stdin.readline())
nodes = {}
for _ in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    nodes[a] = Node(a, b, c)

root = 1
end = 0
cnt = 0
visited = set()

inorder(1)
dfs(1)
