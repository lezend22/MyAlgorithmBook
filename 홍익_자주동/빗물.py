import sys

h, w = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

maxh = 1
maxl = 0
maxIndex = 0

for i in range(len(arr)):
    if arr[i] > maxh:
        maxh = arr[i]
        maxIndex = i

total = 0
temp = 0
for i in range(maxIndex+1):
    if arr[i] > temp:
        temp = arr[i]
    total += temp
temp = 0
for i in range(w-1, maxIndex, -1):
    if arr[i] > temp:
        temp = arr[i]
    total+=temp

print(total - sum(arr))


# pivot = arr[0]
# max = arr[0]
# remain = []
# result = 0
# resolve = []
#
#
# for i in range(1, len(arr)):
#
#     if arr[i] < pivot:
#         if arr[i] > max:
#             max = arr[i]
#         remain.append(arr[i])
#     else:
#         if remain != None:
#             for r in remain:
#                 result += (pivot - r)
#         pivot = arr[i]
#         max = 0
#         remain = []
#
# temp = 0
#
# for r in range(len(remain)-1, 0-1, -1):
#     if remain[r] > temp:
#         resolve.append(r)
#         temp = remain[r]
#     else:
#         for i in resolve:
#             remain.pop(i)
#         break
#
#
# for r in remain:
#     result += (max-r)
#
# print(result)



# remain = []
# resolve = []
# result = 0
#
# pivot = arr[0]
# for i in range(1, len(arr)):
#
#     if pivot > arr[i]:
#         max = arr[i]
#         for j in range(i, len(arr)):
#             # pivot보다 크거나 같을때
#             if arr[j] >= pivot:
#                 print("break here! j=", j)
#                 max = arr[j]
#                 pivot = arr[j]
#                 i = j
#                 break
#             if arr[j] > max:
#                 max = arr[j]
#
#             remain.append(arr[j])
#             i = j
#
#         print(remain)
#
#
#         for k in remain:
#             result += (k-max)
#
#     else:
#         print("else")
#         pivot = arr[i]
#
# print(result)