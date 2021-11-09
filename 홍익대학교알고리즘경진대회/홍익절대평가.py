import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
x, y = map(int, sys.stdin.readline().split())

yans = 0
xans = int(n * (0.01 * x))

for i in arr:
    if i >= y:
        yans += 1

print(xans, yans)
