from collections import defaultdict

answer = 1e9
def solution(alp, cop, problems):

    global answer

    graph = defaultdict(list)
    s = [alp, cop, 1, 1, 1]
    problems = [s] + problems
    problems.sort()

    for i in range(len(problems)):
        for j in range(i+1, len(problems)):
            graph[i].append((j, problems[j]))

    print(graph)

    def getMinCost(now_alp, now_cop, current, dest):

        needalp = dest[0] - now_alp
        needcop = dest[1] - now_cop

        if needalp <= 0 and needcop <= 0:
            return now_alp, now_cop, 0

        alpmok = needalp // current[2]
        copmok = needcop // current[3]
        if needalp % current[2]:
            alpmok += 1
        if needcop % current[3]:
            copmok += 1

        retmok = max(alpmok, copmok)
        nogada = needalp + needcop

        plusalp = retmok * current[2]
        pluscop = retmok * current[3]

        if retmok <= nogada:
            return now_alp + plusalp, now_cop + pluscop, retmok * current[4]
        else:
            return now_alp + plusalp, now_cop + pluscop, nogada

    def dfs(falp, fcop, start, cost, cnt):
        global answer

        if cnt == len(problems):
            answer = min(answer, cost)
            return

        for node in graph[start]:
            idx, dest = node

            now_alp, now_cop = falp, fcop
            print("SEX", start, idx)
            nalp, ncop, ret = getMinCost(now_alp, now_cop, problems[start], dest)
            print(nalp, ncop, ret)

            if ret:
                dfs(nalp, ncop, idx, cost + ret, cnt + 1)
            else:
                dfs(nalp, ncop, idx, cost, cnt + 1)

    dfs(alp, cop, 0, 0, 1)

    print(answer)
    return answer

solution(0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]])