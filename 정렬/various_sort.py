import sys

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def selectSort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def insertSort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break

def quickSort(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[right], arr[left] = arr[left], arr[right]
    quickSort(arr, start, right-1)
    quickSort(arr, right+1, end)

    ###일반적으로 데이터 특성을 파악하기 힘들면 퀵정렬 사용


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    tail = arr[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

def countSort():
    arr = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
    count = [0] * (max(arr)+1)

    for i in range(len(arr)):
        count[arr[i]] += 1

    for i in range(len(count)):
        for j in range(count[i]):
            print(i, end=' ')

    ###데이터의 크기 차이(max, min)가 심한 경우 심각한 메모리 비효율성
    ###데이터의 범위가 한정되어있고 동일한 값을 갖는 데이터가 여러개 나올 때 적합
    ###O(N+K) K는 max(데이터)크기



if __name__ == '__main__':
    countSort()

