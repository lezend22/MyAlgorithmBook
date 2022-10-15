def check(pivot, dat):
    # true 일때 유통기한 안쪽
    # false 이면 유통기한 초과
    pa, pb, pc = pivot
    ra, rb, rc = dat
    if pa > ra:
        return True
    elif pa == ra:
        if pb > rb:
            return True
        elif pb == rb:
            if pc <= rc:
                return False
            else:
                return True

    return False

def solution(today, terms, privacies):

    dic = {}
    answer = []

    pa, pb, pc = map(int, today.split("."))
    print("p", pa, pb, pc)
    for term in terms:
        a, b = term.split()
        dic[a] = int(b)

    for idx, privacy in enumerate(privacies):
        day, val = privacy.split()
        a, b, c = map(str, day.split("."))
        b = b.lstrip('0')
        ra, rb, rc = int(a), int(b), int(c)


        t = rb
        if rc == 1:
            rc = 28
            t -= 1
        else:
            rc -= 1

        t = t + dic[val]
        while t > 12:
            ra += 1
            t = t - 12
        rb = t

        print("SEX",ra, rb, rc)
        # flag = False
        # if pa > ra:
        #     flag = True
        # elif pa == ra:
        #     if pb > rb:
        #         flag = True
        #     elif pb == rb:
        #         if pc < rc:
        #             flag = True
        if check((pa, pb, pc), (ra, rb, rc)):
            answer.append(idx+1)

    return answer

print(solution(
"2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))