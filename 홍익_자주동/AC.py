import sys
from collections import deque

t = int(sys.stdin.readline())


for i in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    arr = deque(sys.stdin.readline().rstrip()[1:-1].split(","))

    if n == 0:
        arr = deque()

    errorType = False
    for j in p:
        if j == 'R':
            arr.reverse()
            # print("arr", arr)
        elif j == 'D':
            if arr:
                arr.popleft()
                # print("arr", arr)
            else:
                print("error")
                errorType = True
                break

    if errorType == False:
        for i in arr:
            ## output공식
            print("[" + ",".join(arr) + "]")


    # for i in range(t):
#     arrT = arr[i]
#     pT = p[i]
#     nT = n[i]
#
#     for j in pT:
#         if j == 'R':
#             reverse = True
#
#         if j == 'D':
#             if reverse == False:
#                 arrT.pop()
#             else:
#                 arrT.poplef



