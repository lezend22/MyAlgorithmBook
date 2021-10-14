# itertools 잘 쓸수 있는지?
# combination 중복x조합
# permutation 중복조합
# product 2개이상 모든 조합
import sys
from itertools import combinations

while True:
    arr = list(map(int, sys.stdin.readline().split()))
    if arr[0] == 0:
        break
    n = arr[0]
    arr.pop(0)

    l = list(combinations(arr, 6))

    for i in l:
        for j in i:
            print(j, end=' ')
        print()
    print()


