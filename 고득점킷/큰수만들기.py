import sys
sys.setrecursionlimit(500000)
answer = ''
def dfs(number, n):
    # print(number, n)
    global answer
    if n == 0:
        return

    max_ = 0
    idx = -1

    for i in range(len(number)-n, -1, -1):
        # print(i, number[i])
        num = int(number[i])
        # print(i, number[i])
        if max_ <= num:
            max_ = num
            idx = i

    answer += number[idx]
    # print(answer)
    if idx + 1 < len(number) and len(number[idx+1:]) > 0:
        dfs(number[idx+1:], n-1)


def solution(number, k):
    global answer
    n = len(number) - k
    dfs(number, n)
    return answer


print("final:", solution("123456", 4))
