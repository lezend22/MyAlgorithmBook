
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
    n = len(box)
    total = sum(box)
    s, e = box[0], int(1e9)

    while s < e:
        print(s, e)
        mid = (s + e) // 2
        if check(mid):
            e = mid - 1
        else:
            s = mid + 1


    return s

print(solution([5, 15, 19]))
# print(solution([10, 3, 5, 7]))