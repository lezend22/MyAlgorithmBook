import sys
from collections import deque


def reverseArr(queue):
    queue.reverse()
    return queue

t = int(sys.stdin.readline())
for _ in range(t):
    p = list(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline())
    arr = str(sys.stdin.readline().rstrip())
    try:
        arr = list(map(int, arr[1:-1].split(",")))
    except:
        arr = arr[1:-1]

    queue = deque(arr)
    flag = False
    reverseCnt = 0
    for f in p:
        if f == 'R':
            reverseCnt += 1
        elif f == 'D':
            if len(queue) == 0:
                print("error")
                flag = True
                break
            if reverseCnt % 2 == 0:
                queue.popleft()
            else:
                queue.pop()
    if not flag:
        if reverseCnt % 2 != 0:
            queue.reverse()
        arr = str(list(queue))
        print(arr.replace(" ", ""))

