from collections import defaultdict
minL = 1e9
answer = [-1, -1]
dic = defaultdict(int)
tic = defaultdict(int)

def solution(gems):
    global minL, answer
    for i in gems:
        dic[i] += 1
    total = len(dic.keys())
    # print(total)
    s, e = 0, 0
    windowSize = 0
    while True:

        if e > len(gems)-1:
            # print("here break")
            break

        if e <= (len(gems)-1):
            e_ = gems[e]
            tic[e_] += 1
            # print(s, e)
        # print(s, e)
        # print(tic)
        if len(tic.keys()) == total:
            while len(tic.keys()) == total:
                temp = e - s
                # print(temp)
                if minL > temp:
                    answer = [s+1, e+1]
                    minL = temp

                if s > len(gems)-1:
                    break
                else:
                    s_ = gems[s]
                    tic[s_] -= 1
                    # print("s가커짐", s, e)
                    # print(tic)
                    if tic[s_] == 0:
                        del tic[s_]
                    s += 1
        e += 1

    return answer
print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))