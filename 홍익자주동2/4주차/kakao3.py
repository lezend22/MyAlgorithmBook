import sys
import datetime
import math
from collections import defaultdict

fees = [1, 461, 1, 10]
records = ["00:00 1234 IN"]
timeFormat = "%H:%M"
def solution(fees, records):

    basicMin, basicFee, unitMin, unitFee = fees
    parking = {}
    parkingTime = defaultdict(int)

    for i in records:
        # 시간, 번호, 출/입
        a, b, c = map(str, i.split())
        if b not in parkingTime:
            parkingTime[b] = 0

        if c == 'IN':
            parking[b] = a

        elif c == 'OUT':
            a_datetime = datetime.datetime.strptime(a, timeFormat)
            pre_datetime = datetime.datetime.strptime(parking[b], timeFormat)
            useTime = a_datetime - pre_datetime
            # print(str(useTime))

            h, m, s = map(int, str(useTime).split(':'))
            # print(h, m, s)
            toMin = h * 60 + m
            parkingTime[b] += toMin

            parking.pop(b)

    for i in parking:
        lastTime = '23:59'
        lastTime = datetime.datetime.strptime(lastTime, timeFormat)
        iTime = datetime.datetime.strptime(parking[i], timeFormat)
        iTime = lastTime - iTime
        h, m, s = map(int, str(iTime).split(':'))
        toMin = h * 60 + m
        parkingTime[i] += toMin

    # print(parkingTime)

    result = []
    for i in parkingTime:
        a1 = parkingTime[i]
        if a1 > basicMin:
            a2 = (a1 - basicMin) / unitMin
            a2 = math.ceil(a2)
            fee = basicFee + a2 * unitFee
            result.append((i, fee))
        else:
            fee = basicFee
            result.append((i, fee))


    result.sort(key=lambda x:x[0])
    result2 = []
    for i in result:
        a, b = i
        result2.append(b)

    return result2



solution(fees, records)