import sys

n, k = sys.stdin.readline().split()
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
result = 0

# for i in range(int(k)):
#     ###쓰레기 코드;; O(N * NlogN)으로 됨;;
#     a.sort()
#     b.sort(reverse=True)
#
#     a[0], b[0] = b[0], a[0]

a.sort()
b.sort(reverse=True)
#   정렬 한번하고 index만 늘리면됨
for i in range(int(k)):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]

print(sum(a))

