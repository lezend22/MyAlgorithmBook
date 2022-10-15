def solution(s):
    answer = len(s)

    for l in range(1, len(s)):
        temp = ""
        cnt = 1
        pivot = s[:l]
        # for i in range(l, len(s), l):
        i = l

        while True:
            if i >= len(s):
                if cnt > 1:
                    temp += str(cnt)
                temp += pivot
                break

            if pivot == s[i:i+l]:
                cnt += 1
            else:
                if cnt == 1:
                    temp += pivot

                if cnt > 1:
                    temp += str(cnt)
                    temp += pivot
                pivot = s[i:i+l]
                cnt = 1

            i += l

        print(temp)
        answer = min(answer, len(temp))

    return answer

print(solution("aabbaccc"))