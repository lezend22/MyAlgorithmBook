from collections import deque


def solution(info, edges):
    graph = [0] * len(info)
    for i in edges:
        a, b = i
        graph[a].append(b)
        graph[b].append(a)

    queue = deque()
    queue.append(0)
    sheep = 1

    while queue:
        popleft = queue.popleft()
        for i in graph[popleft]:
            if info[i] == 1:
                sheep -= 1
                if sheep <= 0:
                    sheep += 1
                    continue
                else:
                    queue.append(i)
            elif info[i] == 0:
                sheep += 1
                queue.append(i)
