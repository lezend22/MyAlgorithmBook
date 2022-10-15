# 다익스트라 사용, 최대 intensity를 갖는 최소 원소를 반환해야함.
# queue에 max_ intensity를 계속 넣지만, heapq에 집어넣어 그 중, 최소가 되는것이 나옴

import heapq
from collections import defaultdict

answer = [0, 1e9]

def solution(n, paths, gates, summits):


    graph = defaultdict(list)

    for path in paths:
        a, b, c = path
        graph[a].append((b, c))
        graph[b].append((a, c))

    summits.sort()
    summits_set = set(summits)

    def getIntense():

        intensity = [1e9] * (n + 1)
        queue = []

        for gate in gates:

            heapq.heappush(queue, (0, gate))
            intensity[gate] = 0

        while queue:

            dist, node = heapq.heappop(queue)

            if node in summits_set or dist > intensity[node]:
                continue

            for nd in graph[node]:
                if nd[0] in gates:
                    continue

                cost = max(intensity[node], nd[1])
                if cost < intensity[nd[0]]:
                    intensity[nd[0]] = cost
                    heapq.heappush(queue, (cost, nd[0]))

        for summit in summits:
            if intensity[summit] < answer[1]:
                answer[0], answer[1] = summit, intensity[summit]

        return answer

    return getIntense()

print(solution(5, [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2], [5]))
