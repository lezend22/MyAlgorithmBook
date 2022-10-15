from collections import defaultdict


def solution(info, query):

    dic = defaultdict(list)
    for i in info:
        k = i.split()
        for lang in [k[0], '-']:
            for loc in [k[1], '-']:
                for mas in [k[2], '-']:
                    for fav in [k[3], '-']:
                        dic[lang+loc+mas+fav].append(int(k[4]))

    for key in dic.keys():
        dic[key].sort()

    answer = []
    for q in query:
        q = q.replace(" and ", " ")
        split = q.split()
        number = int(split.pop())
        join = "".join(split)
        len1 = len(dic[join])
        s, e = 0, len1 - 1
        while s <= e:
            # print(s, e)
            mid = s + (e - s) // 2
            if dic[join][mid] < number:
                s = mid + 1
            else:
                e = mid - 1

        answer.append(len1 - s)
    return answer

print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))
