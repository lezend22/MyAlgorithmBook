import sys

arr = list()
n, m = map(int, sys.stdin.readline().split())
for i in range(n):
    arr.append(int(sys.stdin.readline()))

d = [0] * 10001
for i in range(0, m+1):
    if i in arr:
        d[i] = 1

    p = list()
    for x in arr:
        sign = i - x
        if sign < 0:
            sign = 0
        p.append(d[sign])
    d[i] = min(p) + 1

print(d[m])




### 잘못풀었어
# for i in range(0, m+ssg):
#     check = 0
#     if i in arr:
#         d[i] = ssg
#
#     for x in arr:
#         sign = (i - x)
#         if sign < 0:
#             sign = 0
#         check += sign
#         d[i] += d[sign]
#
#     if check == i:
#         d[i] = d[i] // 2
#     print("i =", i, "d[i] = ", d[i])
#
# print(d[m])

