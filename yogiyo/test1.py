def solution(stack1, stack2, stack3):
    # write your code in Python 3.8.10

    temp = []
    for i in stack1:
        temp.append((i, 1))

    for i in stack2:
        temp.append((i, 2))

    for i in stack3:
        temp.append((i, 3))

    temp.sort(reverse=True)
    ans = [str(x[1]) for x in temp]

    return "".join(ans)

print(solution([2, 7], [4, 5], [1]))