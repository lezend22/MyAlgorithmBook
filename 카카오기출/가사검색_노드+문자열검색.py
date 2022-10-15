# 내가 짠 노드
from collections import defaultdict


class Node:
    def __init__(self):
        self.cnt = defaultdict(int)
        self.next = {}

class Tree:

    def __init__(self, Node):
        self.head = Node

    def add(self, word, s):
        if not s:
            word = word[::-1]

        cur = self.head
        for i in range(len(word)):
            cur.cnt[len(word)] += 1
            if word[i] in cur.next:
                cur = cur.next[word[i]]
            else:
                cur.next[word[i]] = Node()
                cur = cur.next[word[i]]

        return

    def find(self, query, flag):
        if not flag:
            query = query[::-1]
        print(query)
        cur = self.head
        for i in range(len(query)):
            if query[i] == '?':
                print(cur.cnt)
                return cur.cnt[len(query)]
            else:
                if query[i] in cur.next:
                    cur = cur.next[query[i]]
                else:
                    return 0


def solution(words, queries):

    tree1 = Tree(Node())
    tree2 = Tree(Node())
    answer = []
    for word in words:
        tree1.add(word, True)
        tree2.add(word, False)

    for query in queries:
        if query[-1] == '?':
            answer.append(tree1.find(query, True))
        else:
            answer.append(tree2.find(query, False))

    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
