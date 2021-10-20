# 이진탐색이라고 같은공식이 있는거아님
# 자꾸 공식안에 문제를 끼워맞출려하지말고 새로운 방식을찾아
# 투포인터 문제, 배열 양쪽에서 포인터가 있는 문제
import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

leftA, rightA = 0, 0
leftP = 0
rightP = n-1
minNum = sys.maxsize

while leftP < rightP:
    sumN = arr[leftP]+arr[rightP]
    if abs(sumN) < minNum:
        leftA = leftP
        rightA = rightP
        minNum = abs(sumN)
    if sumN > 0:
        rightP -= 1
    elif sumN < 0:
        leftP += 1
    else:
        break
print(arr[leftA], arr[rightA])

