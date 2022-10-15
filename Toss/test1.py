def solution(s):
    s1 = []
    for i in s:
        s1.append(int(i))
    s1.sort(reverse=True)
    pos = []
    i = 0
    endFlag = False
    while i < len(s1):
        pivot, start = s1[i], i
        flag = False
        for j in range(3):
            idx = i + j
            if idx >= len(s1):
                endFlag = True
                break
            if pivot != s1[idx]:
                flag = True
                break
        if endFlag:
            break

        if flag:
            i += 1
            continue

        else:
            print(s1[start:start+3], start)
            pos.append(s1[start:start+3])
            i += 1

    print(pos)

    if not pos:
        answer = -1
    else:
        temp = ''
        for k in pos[0]:
            temp += str(k)
        answer = int(temp)

    return answer

print(solution("1231321121"))