import sys

class Node():
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def preOrder(root):
    print(nodes[root].data, end="")
    if nodes[root].left != '.':
        preOrder(nodes[root].left)
    if nodes[root].right != '.':
        preOrder(nodes[root].right)

def inOrder(root):
    if nodes[root].left != '.':
        inOrder(nodes[root].left)
    print(nodes[root].data, end="")
    if nodes[root].right != '.':
        inOrder(nodes[root].right)

def postOrder(root):
    if nodes[root].left != '.':
        postOrder(nodes[root].left)
    if nodes[root].right != '.':
        postOrder(nodes[root].right)
    print(nodes[root].data, end="")


n = int(sys.stdin.readline())
nodes = {}
for _ in range(n):

    a, b, c = map(str, sys.stdin.readline().rstrip().split())
    nodes[a] = Node(a, b, c)

preOrder('A')
print()
inOrder('A')
print()
postOrder('A')
