from collections import defaultdict


def solution(words, queries):

    answer = []
    dic1 = defaultdict(dict)
    dic2 = defaultdict(dict)
    for word in words:
        s = len(word)
        print(word, s)
        for i in range(1, s):
            w1, w2 = word[:i], word[i:]
            if dic1[w1].get(len(w2), 0):
                dic1[w1][len(w2)] += 1
            else:
                dic1[w1][len(w2)] = 1

            if dic2[w2].get(len(w1), 0):
                dic2[w2][len(w1)] += 1
            else:
                dic2[w2][len(w1)] = 1

    print(dic1)
    print(dic2)
    for query in queries:
        origin = len(query)

        ans = 0
        if query[-1] == '?':
            query = query.replace("?", "")
            if len(query) == 0:
                for key in dic1.keys():
                    if dic1[key].get(len(query), 0):
                        ans += dic1[key][len(query)]
            else:
                q = origin - len(query)
                if dic1[query].get(q, 0):
                    ans = dic1[query][q]
        else:
            query = query.replace("?", "")
            q = origin - len(query)
            if dic2[query].get(q, 0):
                ans = dic2[query][q]

        answer.append(ans)

    # print(answer)
    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))