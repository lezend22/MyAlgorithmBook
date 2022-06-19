import sys
from collections import deque

#키보드 구성
l1 = "qwert"
l2 = "asdfg"
l3 = "zxcv"

r1 = " yuiop"
r2 = " hjkl"
r3 = "bnm"

arr1 = []
arr1.append(l1)
arr1.append(l2)
arr1.append(l3)

arr2 = []
arr2.append(r1)
arr2.append(r2)
arr2.append(r3)

dic1 = {}
dic2 = {}
for i in range(len(arr1)):
    for j in range(len(arr1[i])):
        dic1[arr1[i][j]] = (i, j)

for i in range(len(arr2)):
    for j in range(len(arr2[i])):
        dic2[arr2[i][j]] = (i, j)

def solution(lf, rf, s):

    spendTime = 0
    lx, ly = dic1[lf]
    rx, ry = dic2[rf]
    queue = deque(s)
    leftPos, rightPos = lf, rf
    while queue:
        nextChar = queue.popleft()
        if leftPos == nextChar:
            # print("left pass")
            continue

        if rightPos == nextChar:
            # print("right pass")
            continue

        if nextChar in dic1.keys():
            nx, ny = dic1[nextChar]
            # print("left occurs", abs(lx - nx) + abs(ly - ny))
            spendTime += abs(lx - nx) + abs(ly - ny)
            leftPos = nextChar
            lx, ly = nx, ny
            continue

        if nextChar in dic2.keys():
            nx, ny = dic2[nextChar]
            # print("right occurs", abs(rx - nx) + abs(ry - ny))
            spendTime += abs(rx - nx) + abs(ry - ny)
            rightPos = nextChar
            rx, ry = nx, ny
            continue

    return spendTime


if __name__ == '__main__':
    lf, rf = map(str, sys.stdin.readline().split())
    s = sys.stdin.readline().rstrip()
    print(solution(lf, rf, s) + len(s))