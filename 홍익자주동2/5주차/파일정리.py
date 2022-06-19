import sys
from collections import defaultdict

n = int(sys.stdin.readline())
dic = defaultdict(list)

for _ in range(n):
    a, b = map(str, sys.stdin.readline().rstrip().split("."))
    dic[b].append(a)

sortArr = []
for i in dic:
    sortArr.append(i)

sortArr.sort()
for i in sortArr:
    print(i, len(dic[i]))
