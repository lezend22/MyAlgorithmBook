from collections import defaultdict


def solution(enroll, referral, seller, amount):

    graph = defaultdict(str)
    graph["-"] = "None"
    money = {}
    money["-"] = 0

    for i in range(len(enroll)):
        graph[enroll[i]] = referral[i]
        money[enroll[i]] = 0

    def count(who, much):

        while True:

            # 종료조건

            # 반복조건
            bbozi = much // 10
            print(bbozi)
            parent = graph[who]
            if bbozi >= 1:
                if parent != "None":
                    rest = much - bbozi
                    money[who] += rest
                    who = parent
                    much = bbozi
                else:
                    break

            else:
                money[who] += much
                break

    for i in range(len(seller)):
        who = seller[i]
        much = amount[i] * 100
        count(who, much)
        print(money)

    # print(money)
    answer = []
    for name in enroll:
        answer.append(money[name])

    return answer

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))
