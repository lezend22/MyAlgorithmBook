def floor_(money):
    if money < 100:
        return 0
    else:
        s_ = str(money)
        s_ = s_[:-2] + "00"
        return int(s_)


def check(threshold, ranksize, maxratio, minratio, money):
    a, b = 0, threshold
    if threshold == 0:
        tax = minratio
    else:
        tax = 0
    flag = False
    money_ = floor_(money)
    while tax <= maxratio:
        # print(a, b, tax)
        if a <= money < b:
            take = money_ * tax * 0.01
            ret = money - int(take)
            return int(ret)

        else:
            a = b
            b = b + ranksize
            if flag:
                tax += 1
            if not flag:
                tax = minratio
                flag = True

    take = money_ * maxratio * 0.01
    ret = money - int(take)
    # print(money, take, maxratio, ret)
    return int(ret)


def solution(money, minratio, maxratio, ranksize, threshold, months):
    # a, b = 최소 최대
    for i in range(months):
        money = check(threshold, ranksize, maxratio, minratio, money)
        # print(money)
    answer = money
    return answer

print(solution(1000000000, 50, 99, 100000, 0, 6))