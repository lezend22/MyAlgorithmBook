import sys

def solution(v):
    ans = []

    x1, x2, y1, y2 = 0, 0, 0, 0
    x1, y1 = v[0][0], v[0][1]
    x1Count = 1
    x2Count = 0
    y1Count = 1
    y2Count = 0
    for i in range(1, 3):
        if v[i][0] != x1:
            x2 = v[i][0]
            x2Count += 1
        else:
            x1Count += 1

        if v[i][1] != y1:
            y2 = v[i][1]
            y2Count += 1
        else:
            y1Count += 1
    if x1Count == 2:
        ans.append(x2)
    else:
        ans.append(x1)
    if y1Count == 2:
        ans.append(y2)
    else:
        ans.append(y1)
    return ans

print(solution())
