import sys

k = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

length = len(arr)
depth = length // 2
midIdx = depth

level = [[] for _ in range(k+1)]
# for i in range(depth)