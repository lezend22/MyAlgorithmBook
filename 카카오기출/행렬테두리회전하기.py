import heapq
from collections import deque


def solution(rows, columns, queries):
    answer = []

    def show():
        for i in arr:
            print(i)
        print()

    arr = [[x for x in range(k*columns + 1, k*columns + 1 + columns)] for k in range(rows)]
    # print(arr)
    for query in queries:
        # show()
        smin = 1e9
        x1, y1, x2, y2 = query
        x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1

        s1 = deque([arr[x][y1] for x in range(x1, x2+1)])
        s2 = deque([arr[x][y2] for x in range(x1, x2 + 1)])
        k1 = deque([arr[x1][y] for y in range(y1 + 1, y2)])
        k2 = deque([arr[x2][y] for y in range(y1 + 1, y2)])

        popleft = s1.popleft()
        k1.appendleft(popleft)
        pop = k1.pop()
        s2.appendleft(pop)
        s__pop = s2.pop()
        k2.append(s__pop)
        k__popleft = k2.popleft()
        s1.append(k__popleft)

        idx = 0
        for x in range(x1, x2 + 1):
            smin = min(smin, s1[idx])
            arr[x][y1] = s1[idx]
            smin = min(smin, s2[idx])
            arr[x][y2] = s2[idx]
            idx += 1

        idx = 0
        for y in range(y1+1, y2):
            smin = min(smin, k1[idx])
            arr[x1][y] = k1[idx]
            smin = min(smin, k2[idx])
            arr[x2][y] = k2[idx]
            idx += 1

        answer.append(smin)


    return answer

print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))