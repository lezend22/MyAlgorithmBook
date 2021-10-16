# 조합이용 해결
# 모음, 자음 집합에서 각각 조합으로 가능한 집합 뽑은후
# sort를 이용 합쳐서 마지막 result까지 sorting하여 정렬
import sys
from itertools import combinations
l, c = map(int, sys.stdin.readline().split())
arr = sys.stdin.readline().rstrip().split(' ')

varr = ''
carr = ''
v1 = []
v2 = []
result = []
#vowel, consonant
vowel = ['a','e','i','o','u']

for i in arr:
    if i in vowel:
        varr += i
    else:
        carr += i

m = len(varr)
if m > l:
    m = l


for i in range(1, m+1):
    n = l-i
    if n < 2:
        break
    temp1 = list(combinations(varr, i))
    temp2 = list(combinations(carr, n))
    for i in temp1:
        r1 = ''.join(i)
        for j in temp2:
            r2 = ''.join(j)
            r3 = r1+r2
            sort = sorted(r3)
            result.append(sort)
result.sort()
for i in result:
    print(''.join(i))

