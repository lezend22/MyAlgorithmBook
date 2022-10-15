from collections import deque


def solution(rc, operations):

    r, c = len(rc), len(rc[0])
    row = deque(deque(row[1:-1]) for row in rc)
    col = [deque(rc[x][0] for x in range(r)), deque(rc[x][c-1] for x in range(r))]

    answer = []

    def show():
        for i in answer:
            print(i)
        print()

    for operation in operations:
        if operation[0] == "R":

            popleft = col[0].popleft()
            row[0].appendleft(popleft)
            row__pop = row[0].pop()
            col[1].appendleft(row__pop)
            col__pop = col[1].pop()
            row[-1].append(col__pop)
            row__popleft = row[-1].popleft()
            col[0].append(row__popleft)

        else:
            pop = row.pop()
            row.appendleft(pop)

            col__pop1, col__pop2 = col[0].pop(), col[1].pop()
            col[0].appendleft(col__pop1)
            col[1].appendleft(col__pop2)


    for i in range(r):
        answer.append([])
        answer[i].append(col[0][i])
        answer[i].extend(row[i])
        answer[i].append(col[1][i])

    show()

    return rc

solution([[0, 0, 0], [1, 1, 1], [2, 2, 2]], ["R", "R","R", "Shif"])
