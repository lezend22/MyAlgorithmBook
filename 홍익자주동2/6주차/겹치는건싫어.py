import sys
from collections import defaultdict

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

p1, p2 = 0, 0
dic = defaultdict(int)
dic[arr[p1]] += 1
flag = -1
result = 0
while True:
    if p1 == len(arr)-1:
        break
    if p2 == len(arr)-1:
        p1 += 1
        result = max(p2-p1+1, result)
        continue
    if flag != -1:
        if arr[p1] == flag:
            flag = -1
        dic[arr[p1]] -= 1
        p1 += 1
        continue
    p2 += 1
    dic[arr[p2]] += 1
    if dic[arr[p2]] > k:
        # print(dic)
        flag = arr[p2]
        continue
    # print(p1, p2)
    result = max(p2-p1+1, result)


print(result)