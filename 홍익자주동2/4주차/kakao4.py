import sys
from itertools import combinations
n = 7
info = [2,3,1,1,0,0,0,0,0,0,0]
source = [x for x in range(10)]


def solution(n, info):

    s, e = 0, 0
    apeach = 0


    for i in range(len(info)):
        if info[i]:
            apeach += (10-i)

    totalChance = []
    while True:
        chance = []
        tn = n
        temp = apeach
        ryan = 0

        if s >= len(info):
            break

        tn -= info[s] + 1
        if tn < 0:
            break

        realPoint = 10 - s
        ryan += realPoint

        if info[s]:
            temp -= realPoint

        e = s+1
        print("here1", s)
        for i in range(e, len(info)):

            #init
            k = i

            while True:
                print("heer2", i)
                if k >= len(info):
                    break

                realPoint = 10 - k
                tn -= (info[k] + 1)
                if tn < 0:
                    break
                if info[k]:
                    temp -= realPoint
                chance.append((k, info[k]+1))
                ryan += realPoint
                k += 1
            print(ryan, temp)
            if ryan >= temp:
                totalChance.append(chance)
        s += 1
        print(s)
    print(totalChance)

solution(n, info)