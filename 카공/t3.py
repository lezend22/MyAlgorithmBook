from itertools import combinations_with_replacement, permutations
import sys
sys.setrecursionlimit(100000)
poss = []
dis = [10, 20, 30, 40]
def dfs(d, n):
    if len(d) == n:
        poss.append(d)
        return
    for i in dis:
        dfs(d + [i], n)

def solution(users, emoticons):
    n = len(emoticons)
    dfs([], n)
    # list_ = list(combinations_with_replacement(dis, n))
    # list2 = list(permutations(dis, n))
    # l = set(list_ + list2)
    # poss = list(l)
    # poss.sort()
    total = []


    for p in poss:
        item = [(p[i], emoticons[i]) for i in range(len(p))]
        plus, sale = 0, 0
        for user in users:
            temp = 0
            for tem in item:
                if tem[0] < user[0]:
                    continue
                temp += (tem[1] // 100 * (100 - tem[0]))

            if temp >= user[1]:
                plus += 1
            else:
                sale += temp
        total.append((plus, sale))

    total.sort(reverse=True)
    # print(total)
    return list(total[0])



print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))