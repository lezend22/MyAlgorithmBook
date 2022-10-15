from collections import defaultdict, deque


def solution(invitationPairs):
    dic = defaultdict(list)
    num = defaultdict(list)
    prior = defaultdict(int)

    pcnt = 0
    for i in invitationPairs:
        a, b = i
        dic[a].append(b)
        if prior[a]:
            continue
        else:
            prior[a] = pcnt
            pcnt += 1

    for i in list(dic.keys()):
        # print(i)
        queue = deque()
        queue.append((i, 0))
        visited = {i}
        num[i] = [0, 0, 0, 0]
        while queue:
            popleft, dist = queue.popleft()
            if dist > 3:
                continue
            if dist != 0:
                num[i][dist] += 1
            for node in dic[popleft]:
                if node not in visited:
                    queue.append((node, dist+1))
                    visited.add(node)

        # print(num[i])
        # break
    ret = []
    for i in list(num.keys()):
        temp = 0
        for k in range(1, len(num[i])):
            if k == 1:
                temp += (10 * num[i][k])
            elif k == 2:
                temp += (3 * num[i][k])
            elif k == 3:
                temp += (1 * num[i][k])

        ret.append((-temp, prior[i], i))


    ret.sort(key=lambda x:(x[0], x[1]))
    print(ret)
    answer = []
    for i in ret:
        answer.append(i[2])
    return answer

# print(solution([[1, 2], [3, 4]]))
print(solution([[1, 2], [1, 3], [3, 4], [4, 5], [4, 6], [4, 7]]))