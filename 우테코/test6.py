import sys
import datetime

def solution(time, plans):
    answer = []
    remainTime = time
    friOut = datetime.datetime(1900,1, 1, 18, 00, 00)
    monIn = datetime.datetime(1900, 1, 1, 13, 00, 00)
    for plan in plans:
        if remainTime < 0:
            remainTime = time
        loc = plan[0]
        s = plan[1]
        e = plan[2]
        pmFormat = "%HPM"
        amFormat = "%HAM"
        if 'A' in s:
            x = datetime.datetime.strptime(s, amFormat)
            x = x.hour


            remainTime -= friOut.hour - x
            if remainTime < 0:
                continue
        else:
            x = datetime.datetime.strptime(s, pmFormat)
            x = x.hour + 12

            if x < friOut.hour:
                remainTime -= friOut.hour - x

        if 'A' in e:
            pass

        else:
            y = datetime.datetime.strptime(e, pmFormat)
            y = y.hour + 12

            if y > monIn.hour:
                remainTime -= y - monIn.hour
        if remainTime >= 0:
            answer.append(loc)
    print(answer)
    return answer[-1]



print(solution(5, [["사이판", "3PM", "5PM"], ["굴락", "2PM", "11AM"]]))