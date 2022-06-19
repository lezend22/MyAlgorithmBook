import sys


n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

### 반복문
# start = 0
# end = max(arr)
# result = 0

# while(start <= end):
#     total = 0
#     mid = (start + end) // 2
#
#     for i in arr:
#         if i > mid:
#             total += (i-mid)
#
#     if total < m:
#         end = mid - ssg
#     else:
#         result = mid
#         start = mid + ssg
#
# print(result)

###재귀
def binarySearch(arr, target, start, end):
    if start > end:
        return None
    total = 0
    mid = (start + end) // 2
    for i in arr:
        if i > mid:
            total += (i - mid)
    if total < target:
        binarySearch(arr, target, start, mid-1)
    else:
        global result
        result = mid
        binarySearch(arr, target, mid+1, end)

binarySearch(arr, m, 0, max(arr))
print(result)
