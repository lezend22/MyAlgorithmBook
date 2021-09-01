import sys

n = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))

def binarySearch(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binarySearch(arr, target, start, mid - 1)
    else:

        return binarySearch(arr, target, mid + 1, end)

if __name__ == '__main__':
    ###이분탐색
    sort = sorted(arr1)

    for i in arr2:

        search = binarySearch(sort, i, 0, n - 1)
        if search == None:
            print("no", end=' ')
        else:
            print("yes", end=' ')

