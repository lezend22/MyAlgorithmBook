from collections import defaultdict

dic = defaultdict(int)
dat = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print(len(dat))
for i in range(1, len(dat)):
    dat[i] += dat[i-1]
print(dat)
date = []

def findCost(k, masks):
    print(masks)
    n = len(masks)
    dp = [[0] * (k + 1) for _ in range(n)]
    for i in range(1, n):
        for j in range(1, k+1):
            w = masks[i][1]
            c = masks[i][0]
            if j < w:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = min(dp[i-1][j-w] + c, dp[i-1][j])

    print(dp)
    print("this", dp[n-1][k])

def solution(masks, dates):
    masks = [[0, 0]] + masks
    for i in dates:
        if len(i) > 10:
            a1, a2 = i.split("~")
            print(a1, a2)
            a, b, c = a1.split("/")
            num1 = int(a) * 365 + dat[int(b)] + int(c)
            a, b, c = a2.split("/")
            num2 = int(a) * 365 + dat[int(b)] + int(c)
            for j in range(num1, num2+1):
                date.append(j)
        else:
            a, b, c = i.split("/")
            num = int(a) * 365 + dat[int(b)] + int(c)
            date.append(num)
    print(date)
    date.sort()
    print(date)
    k, pivot = 1, date[0]
    i = 1
    while True:
        print("index", i)
        if date[i] == pivot + 1:
            k += 1
            pivot = date[i]
            print(i, k)
            i += 1
        else:
            pivot = date[i]
            print("her", i, k)
            findCost(k, masks)
            k = 1
            i += 1
        if i >= len(date):
            findCost(k, masks)
            break

solution([[3200, 4], [2300, 2], [1100, 1], [4200, 6]], ["2022/05/02", "2022/05/01", "2022/05/07", "2022/05/05", "2022/05/08", "2022/05/13~2022/05/15", "2022/05/14~2022/05/17", "2022/05/01~2022/05/02", "2022/05/16"])
