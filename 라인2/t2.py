from collections import defaultdict


class Node:
    def __init__(self):
        self.cnt = defaultdict(int)
        self.next = {}


class Tree:
    def __init__(self, Node):
        self.head = Node

    def add(self, word):

        cur = self.head
        for i in range(len(word)):
            cur.cnt[len(word)] += 1
            if word[i] in cur.next:
                cur = cur.next[word[i]]
            else:
                cur.next[word[i]] = Node()
                cur = cur.next[word[i]]

        return

    def find(self, query, k):

        cur = self.head
        for i in range(len(query)):
            if query[i] == '.':
                for key in cur.cnt.keys():
                    if key >= len(query[i:]) - 1:
                        return True
            else:
                if query[i] in cur.next:
                    cur = cur.next[query[i]]
                else:
                    return False

        return True

from typing import List

def solution(k: int, dic: List[str], chat: str) -> str:
    answer = ''
    tree1 = Tree(Node())

    for word in dic:
        tree1.add(word)

    for query in chat:
        tree1.find(query, k)


    return answer

