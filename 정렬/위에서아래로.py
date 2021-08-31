import sys

n = int(input())
arr = list()
for i in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

arr.sort(reverse=True)

for i in arr:
    print(i, end=' ')
