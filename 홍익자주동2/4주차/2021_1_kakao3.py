
class Node:
    def __init__(self):
        self.num = None
        self.prev = None
        self.next = None
        self.empty = False

def solution(n, k, cmd):

    linkedList = [Node() for _ in range(n)]

    for i in range(1, n):
        linkedList[i].num = i
        linkedList[i].prev = linkedList[i-1]
        linkedList[i-1].next = linkedList[i]

    linkedList[0].num = 0
    curr = linkedList[k]
    stack = []
    for cm in cmd:
        # print(cm)
        if cm[0] == "U":
            num = int(cm[2:])
            for _ in range(num):
                curr = curr.prev

        elif cm[0] == "D":
            num = int(cm[2:])
            for _ in range(num):
                curr = curr.next

        elif cm[0] == "C":
            stack.append(curr)
            curr.empty = True

            up = curr.prev
            down = curr.next

            if up:
                up.next = down
            if down:
                down.prev = up
                curr = down
            else:
                curr = up

        elif cm[0] == "Z":
            pop = stack.pop()
            pop.empty = False

            up = pop.prev
            down = pop.next

            if up:
                up.next = pop
            if down:
                down.prev = pop

        # print(curr.num)
    answer = ""
    for i in range(n):
        if linkedList[i].empty == True:
            answer += 'X'
        else:
            answer += 'O'
    print(answer)
solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])