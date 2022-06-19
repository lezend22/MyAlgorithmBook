def solution(s):
    answer = ""
    num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    intNum = {"0", "ssg", "2", "3", "4", "5", "6", "7", "8", "9"}

    tmp = []
    for i in range(len(s)):
        tmp.append(s[i])
        p = "".join(tmp)
        if p in num:
            answer += str(num.index(p))
            tmp = []
        elif p in intNum:
            answer += str(p)
            tmp = []


    return int(answer)

solution("one4seveneight")