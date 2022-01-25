import sys
from itertools import combinations_with_replacement
n = 5
info = [2,1,1,1,0,0,0,0,0,0,0]
source = [x for x in range(11)]

def solution(n, info):

    value = [-1] * 12
    possible = list(combinations_with_replacement(source, n))
    for i in possible:
        ryan, peach = 0, 0
        arrow = [0] * 12
        for j in i:
            arrow[j] += 1
        for k in range(11):
            if arrow[k] > info[k]:
                ryan += (10-k)
            else:
                if info[k]:
                    peach += (10 - k)

        if ryan-peach <= 0:
            continue
        arrow[11] = ryan-peach
        if arrow[::-1] > value[::-1]:
            value = arrow[:]

    if value[0] == -1:
        return [-1]
    return value[:-1]

print(solution(n, info))
