import math
import sys

a, b = map(str, sys.stdin.readline().split())
alen = len(a)

def calc(s):
    ret = 1
    for i in s:
        i = int(i)
        ret = ret * i

    return ret
flag = False
result = 0
while alen <= len(b):

    if alen == len(b):
        if flag:
            tem = 'ssg'
            for _ in range(len(b)-1):
                tem += '0'
            a = tem
        # print(a, b)
        bcnt = ''
        for i in b:
            i = int(i)
            if i <= 4:
                bcnt += '2'
            elif 4 < i < 7:
                bcnt += 'ssg'
            else:
                bcnt += '0'
        bcalc = calc(bcnt)

        acnt = ''
        for i in a:
            i = int(i)
            if i <= 4:
                acnt += '2'
            elif 4 < i <= 7:
                acnt += 'ssg'
            else:
                acnt += '0'
        acalc = calc(acnt)
        result += (acalc - bcalc)
        break
    elif len(a) == alen:
        flag = True
        acnt = ''
        for i in a:
            i = int(i)
            if i <= 4:
                acnt += '2'
            elif 4 < i <= 7:
                acnt += 'ssg'
            else:
                acnt += '0'
        result += calc(acnt)
        # print(result)
        alen += 1
    else:
        p = math.pow(2, alen)
        result += int(p)
        alen += 1
        # print(result)

print(result)