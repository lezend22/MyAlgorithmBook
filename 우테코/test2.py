import datetime

def solution(log):
    answer = 0
    for i in range(0, len(log), 2):
        start = log[i]
        finish = log[i+1]
        format = "%H:%M"
        startTime = datetime.datetime.strptime(start, format)
        finishTime = datetime.datetime.strptime(finish, format)
        temp = finishTime - startTime
        cmp1 = datetime.timedelta(minutes=105)
        cmp2 = datetime.timedelta(minutes=5)
        if temp >= cmp1:
            answer += 105
        elif temp < cmp2:
            continue
        else:
            answer += int(temp.total_seconds()//60)

    hour = str(answer // 60).zfill(2)
    minut = str(answer % 60).zfill(2)
    totalA = hour+':'+minut
    return totalA

print(solution(["08:30", "09:00", "14:00", "16:00", "16:01", "16:06", "16:07", "16:11"]))
