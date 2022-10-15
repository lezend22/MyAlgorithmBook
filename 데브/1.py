def solution(openA, closeB):
    check = [0] * 5001
    for i in openA:
        check[i] = 1
    for i in closeB:
        check[i] = 2

    arr = openA + closeB
    arr.sort()


    ans, start = 0, 0
    flag = False
    for i in arr:
        if check[i] == 1 and not flag:
            flag = True
            start = i
        elif check[i] == 2:
            if flag:
                ans += (i - start)
                flag = False


    print(ans)
    answer = 0
    return answer

solution([3, 5, 7], [4, 10, 12])