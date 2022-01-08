
def solution(arr):
    answer = [0] * 3
    count = [0] * 3
    for i in range(len(arr)):
        if arr[i] == 1:
            count[0] += 1
        elif arr[i] == 2:
            count[1] += 1
        elif arr[i] == 3:
            count[2] += 1

    m = max(count)
    for i in range(3):
        if count[i] == m:
            continue
        else:
            j = m - count[i]
            answer[i] = j

    return answer

print(solution([3]))