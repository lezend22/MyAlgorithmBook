from itertools import permutations


def solution(n, weak, dist):

    leng = len(weak)
    for i in range(leng):
        weak.append(weak[i] + n)

    # print(weak)
    min_ = leng + 1
    # 시작점 처음부터 하나씩
    for start in range(leng):
        # 가능한 친구 배치 수

        for friend in list(permutations(dist, len(dist))):
            count = 1
            end = friend[count-1] + weak[start]
            for idx in range(start, start + leng):
                if weak[idx] > end:
                    count += 1
                    if count > len(dist):
                        break
                    end = friend[count-1] + weak[idx]
            min_ = min(min_, count)

    if min_ > leng:
        return -1

    return min_

print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))