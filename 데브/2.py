from datetime import datetime
import pandas as pd


def check(data, holidays):
    date_, _ = data.split()
    yy, mm, dd = date_.split("-")
    if mm + '/' + dd in holidays:
        return 0

    dt = datetime(int(yy), int(mm), int(dd))
    # print(dt)
    if dt.weekday() > 4:
        return 0

    return 1


def solution(join_date, resign_date, holidays):
    a, b, c = join_date.split("/")
    c, d = c.split()
    start = a + '-' + b + '-' + c

    r1, r2, r3 = resign_date.split("/")
    end = r1 + '-' + r2 + '-' + r3

    date_range = pd.date_range(start, end)
    answer = 0
    for i in date_range:
        answer += check(str(i), holidays)

    # print(answer)
    return answer

solution("0001/12/01 SUN", "0003/03/02", ["01/02", "12/24", "03/01"])