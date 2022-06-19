
def parse(time):
    a, b, c = time.split(":")
    value = int(a) * 3600 + int(b) * 60 + int(c)
    return value

def goDigit(val):
    a = val // 3600
    b = (val % 3600) // 60
    c = val % 3600 % 60
    ret = str(a).zfill(2) +":"+ str(b).zfill(2) +":"+ str(c).zfill(2)
    return ret


def solution(play_time, adv_time, logs):
    answer = 0
    playLength = parse(play_time)
    adv_length = parse(adv_time)
    dp = [0] * (playLength + 1)
    # print(playLength, adv_length)
    for i in logs:
        a, b, = i.split("-")
        start = parse(a)
        end = parse(b)
        # print(start, end)
        dp[start] += 1
        dp[end] -= 1

    for i in range(1, playLength):
        dp[i] = dp[i] + dp[i-1]

    for i in range(1, playLength):
        dp[i] = dp[i] + dp[i-1]

    maxVal = 0
    for i in range(adv_length-1, playLength):
        temp = dp[i] - dp[i-adv_length]
        if temp > maxVal:
            maxVal = temp
            answer = i-adv_length+1


    return goDigit(answer)

print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))