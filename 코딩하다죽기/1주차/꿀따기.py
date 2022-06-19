import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
answer = 0

pivot1 = sum(arr[1:])
pivot2 = sum(arr[:-1])
b = sum(arr[1:])
b2 = 0
for i in range(1, len(arr)-1):
    # hive 오른쪽끝
    a = pivot1 - arr[i]
    b -= arr[i]
    # print(b)

    # hive 왼쪽끝
    a2 = pivot2 - arr[i]
    b2 += arr[i-1]

    if a+b > answer:
        answer = a + b
    if a2+b2 > answer:
        answer = a2 + b2


a3 = 0
b3 = sum(arr[:-1])
# hive 가운데 끼어있을 때
for i in range(1, len(arr)-1):
    a3 += arr[i]
    b3 -= arr[i-1]
    # b3 = sum(arr[i:-1])
    # print(p3, b3)
    if a3+b3 > answer:
        answer = a3 + b3

print(answer)