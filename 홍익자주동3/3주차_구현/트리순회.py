import sys
sys.setrecursionlimit(50000)

class Node():
    def __init__(self):
        self.num = None
        self.left = None
        self.right = None
        self.parent = None

n = int(sys.stdin.readline())
nodes = [Node() for _ in range(n+1)]

for _ in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    nodes[a].num = a
    nodes[a].left = b
    nodes[a].right = c


def inorder(root):

    global end

    if root == -1:
        return
    inorder(nodes[root].left)
    end = nodes[root].num
    inorder(nodes[root].right)


def simOrder(root):
    global cnt

    if nodes[root].left != -1:
        simOrder(nodes[root].left)
        cnt += 1
    if root == end:
        print(cnt)
        exit(0)
    cnt += 1
    if nodes[root].right != -1:
        simOrder(nodes[root].right)
        cnt += 1


if __name__ == '__main__':
    end = -1
    inorder(1)
    cnt = 0
    simOrder(1)

