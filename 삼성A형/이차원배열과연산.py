from collections import defaultdict

r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]

def getRstack(stack):
    maxI = -1
    for s in stack:
        maxI = max(maxI, len(s))
    if maxI > 100:
        maxI = 100
    ret = [[0] * maxI for _ in range(rowl)]
    x = 0
    for s in stack:
        y = 0
        for yoso in s:
            if y >= maxI:
                break
            ret[x][y] = yoso
            y += 1
        x += 1

    return ret


def R(arr):
    stack = []
    for row in arr:
        ty = 0
        dic = defaultdict(int)
        for i in row:
            if i == 0:
                continue
            dic[i] += 1
        t = []
        for key, value in dic.items():
            t.append((value, key))
        t.sort()
        temp = []
        for k, v in t:
            temp += [v, k]
        stack.append(temp)
    ret = getRstack(stack)
    return ret


def getStack(stack):
    maxI = -1
    for s in stack:
        maxI = max(maxI, len(s))
    if maxI > 100:
        maxI = 100
    ret = [[0] * columnl for _ in range(maxI)]
    y = 0
    for s in stack:
        x = 0
        for yoso in s:
            if x >= maxI:
                break
            ret[x][y] = yoso
            x += 1
        y += 1

    return ret


def C(arr):
    stack = []
    for i in range(columnl):
        dic = defaultdict(int)
        for j in range(rowl):
            if arr[j][i] == 0:
                continue
            dic[arr[j][i]] += 1
        t = []
        for key, value in dic.items():
            t.append((value, key))
        t.sort()
        temp = []
        for k, v in t:
            temp += [v, k]
        stack.append(temp)

    ret = getStack(stack)
    return ret


answer = 0
flag = False
while True:
    rowl, columnl = len(arr), len(arr[0])
    if 0 <= r-1 < rowl and 0 <= c-1 < columnl and arr[r-1][c-1] == k:
        break
    if answer > 100:
        flag = True
        break
    if rowl >= columnl:
        arr = R(arr)
        # print(arr)
    else:
        arr = C(arr)
        # print(arr)
    answer += 1


if not flag:
    print(answer)
else:
    print(-1)
