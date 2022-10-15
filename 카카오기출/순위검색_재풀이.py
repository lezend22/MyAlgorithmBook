from collections import deque
from copy import deepcopy


class Node:
    def __init__(self, data):
        self.data = data
        self.next = {}

class Linkedlist:
    def __init__(self, Node):
        self.head = Node

link = Linkedlist(Node(0))
cnt = 0

def insert(cur, queue):

    if len(queue) == 1:
        number = queue.popleft()
        cur.next[number] = 1
        return

    popleft = queue.popleft()
    if cur.next.get(popleft, 0):
        insert(cur.next[popleft], queue)

    else:
        cur.next[popleft] = Node(queue)
        cur = cur.next[popleft]
        insert(cur, queue)

def find(cur, queue):
    global cnt
    if len(queue) == 1:
        number = queue.popleft()
        for node in cur.next.keys():
            if int(node) >= int(number):
                print(int(node), ">=", int(number))
                cnt += 1
        return

    popleft = queue.popleft()
    if popleft == '-':
        for node in cur.next.keys():
            temp = deepcopy(queue)
            find(cur.next[node], temp)

    else:
        if cur.next.get(popleft, 0):
            find(cur.next[popleft], queue)
        else:
            return


def solution(info, query):
    global cnt
    answer = []
    for i in info:
        l_ = list(map(str, i.split(" ")))
        queue = deque(l_)
        cur = link.head
        insert(cur, queue)

    for q in query:
        cnt = 0
        a, b, c, d = map(str, q.split(" and "))
        d, e = d.split()
        queue = deque([a, b, c, d, e])
        cur = link.head
        find(cur, queue)
        print(cnt)
        answer.append(cnt)

    return answer


print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))