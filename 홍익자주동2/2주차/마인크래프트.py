import sys

n, m, b = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# maxh, minh = 0, 256
# for i in arr:
#     for j in i:
#         minh = min(minh, j)
#         maxh = max(maxh, j)

# def confirm(h):
#     tb = b
#     cnt = 0
#
#     for i in range(n):
#         for j in range(m):
#
#             if arr[i][j] != h:
#                 if h > arr[i][j]:
#
#                     addb = h - arr[i][j]
#                     tb = tb - addb
#                     cnt += addb
#                 elif h < arr[i][j]:
#
#                     digb = arr[i][j] - h
#                     tb = tb + digb
#                     cnt += digb * 2
#     if tb < 0:
#         return -1
#     return cnt
#


maxt = int(1e9)
maxh = 256
for h in range(257):

    cnt = 0
    addb = 0
    digb = 0

    for i in range(n):
        for j in range(m):
            if arr[i][j] < h:
                addb += h - arr[i][j]
            elif arr[i][j] > h:
                digb += arr[i][j] - h
    if addb > digb + b:
        continue
    cnt = (digb * 2) + addb
    if cnt <= maxt:
        maxt = cnt
        maxh = h

print(maxt, maxh)




    # ####
    # v = confirm(h)
    # if v == -1:
    #     continue
    # if v == 0:
    #     maxt = v
    #     mh = arr[0][0]
    #     break
    # if v <= maxt:
    #     maxt = v
    #     mh = h



