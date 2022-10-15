def solution(lottos, win_nums):
    zero = 0
    cnt = 0
    win_nums_set = set(win_nums)
    for number in lottos:
        if number == 0:
            zero += 1
        else:
            if number in win_nums_set:
                cnt += 1

    # all zero correct
    max_ = cnt + zero
    min_ = cnt - zero
    rate = [6, 6, 5, 4, 3, 2, 1]

    answer = [rate[max_], rate[min_]]

    return answer