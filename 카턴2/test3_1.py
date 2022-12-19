n = 0
total = 0

def check(pivot):

    p = pivot * (n - 1)
    temp = total - p
    if temp > pivot:
        return False

    return True

def solution(box):
    global n, total

    total = sum(box)
    n = len(box)
    s, e = 1, int(1e9)

    while s < e:

        mid = (s + e) // 2
        flag = check(mid)
        print(s, e, mid, flag)
        if flag:
            e = mid
        else:
            s = mid + 1

    return e

# print(solution([1, 5, 7, 6]))
# print(solution([5, 15, 19]))
# print(solution([3, 8, 11, 7]))
# print(solution([5, 9, 3, 2, 1]))
print(solution([2, 3, 5, 10, 3, 4, 9]))
