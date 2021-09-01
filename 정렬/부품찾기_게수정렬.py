import sys

n = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))


array = [0] * int(max(arr1)+1)

for i in range(n):
    array[arr1[i]] += 1

# for i in range(len(array)):#0부터 maxNum까지
#     for j in range(array[i]):#각 번호의 개수
#         print(i, end=' ')

print(array)

for i in arr2:
    if array[i] != 0:
        print("yes")
    else:
        print("no")



