import sys

# 데이터가 정렬되어있어야함
# O(logN)
# 데이터 탐색 범위가 2000만 이상일 시, 이진탐색 사용


#재귀
def binarySearch(arr, target, start, end):

    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binarySearch(arr, target, start, mid - 1)
    else:
        return binarySearch(arr, target, mid + 1, end)


#반복문
def binary_search(arr, target, start, end):

    while start <= end:

        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid -1
        else:
            start = mid + 1

    return None

if __name__ == '__main__':

    n, target = list(map(int, sys.stdin.readline().split()))
    array = list(map(int, sys.stdin.readline().split()))

    result = binary_search(array, target, 0, n-1)

    if result == None:
        print("어딧어!")
    else:
        print(result+1)

