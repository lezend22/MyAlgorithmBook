import sys
from collections import defaultdict
id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3

def solution(id_list, report, k):
    length = len(id_list)
    user, visited = {}, {}
    for i in range(length):
        user[id_list[i]] = i
        visited = defaultdict(list)


    reportCnt = [0] * length
    for i in report:
        a, b = map(str, i.split())
        # print(a, b)
        if a not in visited[b]:
            reportCnt[user[b]] += 1
            visited[b].append(a)

    result = [0] * length
    for i in range(len(reportCnt)):
        if reportCnt[i] >= k:
            for j in visited[id_list[i]]:
                result[user[j]] += 1

    return result




print(solution(id_list, report, k))