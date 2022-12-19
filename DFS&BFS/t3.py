import heapq
from collections import defaultdict

visited = 0
ans = []
org = -1

def getJob(queue, tFlag):
    global visited, ans, org

    if tFlag:
        rettime = 0
        ret = []
        for x in queue:
            if x[2] != org:
                ret.append(x)
            else:
                rettime += x[1]
                visited += 1

        if rettime:
            return rettime, ret

    dic = defaultdict(int)
    rettime = 0
    for x in queue:
        dic[x[2]] += x[3]

    temp = []
    for t in dic.keys():
        temp.append((-dic[t], t))
        heapq.heappush(temp, (-dic[t], t))

    g = heapq.heappop(temp)
    org = g[1]
    ret = []

    for x in queue:
        if x[2] != org:
            ret.append(x)
        else:
            visited += 1
            rettime += x[1]

    ans.append(org)

    return rettime, ret


def solution(jobs):
    global ans, org

    turn = 0
    timeset = 0
    queue = []
    flag = False
    start = defaultdict(list)
    tFalg = False
    for job in jobs:
        start[job[0]].append(job)

    while True:

        if visited == len(jobs):
            break

        if start[turn]:
            for x in start[turn]:
                if x[2] == org:
                    tFalg = True
                queue.append(x)

        if timeset:
            timeset -= 1

        if not timeset:
            flag = False

        if not flag and queue:
            timeset, queue = getJob(queue, tFalg)
            tFalg = False
            flag = True

        turn += 1
        print(turn, visited, queue, timeset)

    return ans

print(solution(
[[1, 5, 2, 3], [2, 2, 3, 2], [3, 1, 3, 3], [5, 2, 1, 5], [7, 1, 1, 1], [9, 1, 1, 1], [10, 2, 2, 9]]))
