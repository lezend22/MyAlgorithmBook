from collections import deque
answer = 1e9
block = []
arr = []
fare = {}
length = 0
def findMin(s):

    block = [1e9] * (length+1)
    queue = deque()
    queue.append((s, 0))

    while queue:
        popleft, cost = queue.popleft()
        # print(popleft, arr)

        for node in arr[popleft]:
            if node == s:
                block[s] = 0
                continue
            temp = cost
            temp += fare[(popleft, node)]
            if block[node] > temp:
                block[node] = temp
                queue.append((node, temp))

    return block

def solution(n, s, a, b, fares):
    global block, arr, answer, length
    arr = [[] for _ in range(n+1)]
    length = n
    for road in fares:
        a1, b1, f = road
        arr[a1].append(b1)
        arr[b1].append(a1)
        fare[(a1, b1)] = f
        fare[(b1, a1)] = f

    firstB = findMin(s)
    # print(firstB)
    minA = firstB[a] + firstB[b]
    # print(minA)
    for i in range(1, n+1):
        if i == s:
            continue
        fBlock = findMin(i)
        # print(i, fBlock)
        cost = fBlock[a] + fBlock[b] + firstB[i]
        # print(cost)
        minA = min(minA, cost)

    return minA


print(solution(6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))