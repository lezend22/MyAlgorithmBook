from collections import defaultdict


def getOut(check):
    ret = True
    for i in check:
        if not check[i]:
            ret = False

    return ret


def solution(S, C):
    # write your code in Python 3.8.10
    dic = defaultdict(int)
    for i in S:
        dic[i] += 1

    check = {}
    for i in dic.keys():
        if dic[i] >= 2:
            check[i] = False

    turn = 0
    for c in C:
        temp = list(S)
        temp.insert(c, '$')
        # print(temp)
        init = set()
        for a in range(c):
            init.add(S[a])
        # print(init)
        for b in range(c, len(S)):
            if S[b] in init:
                check[S[b]] = True
        turn += 1
        if getOut(check):
            break

    if not len(check):
        return 0
    if getOut(check):
        return turn
    else:
        return -1

print(solution('abcd', [1, 2]))