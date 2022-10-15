
from typing import List

def get_pow(pivot):
    i = 0
    while True:
        if pow(2, i) > pivot:
            break
        i += 1

    return pow(2, i)


def solution(queries: List[List[int]]) -> int:

    dic = {}
    cnt = 0
    for query in queries:
        a, b = query

        # 있는지 먼저 확인
        if dic.get(a, 0):
            if dic[a][0] + b <= dic[a][1]:
                dic[a][0] += b
                continue
            else:
                ret = get_pow(dic[a][0] + b)
                cnt += dic[a][0]
                dic[a] = (dic[a][0] + b, ret)

        # 없으면
        else:
            pow = get_pow(b)
            dic[a] = [b, pow]

    # print(cnt)
    answer = cnt
    return answer

print(solution([[2, 10], [7, 1], [2, 5], [2, 9], [7, 32]]))