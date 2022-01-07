import sys

n, k = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))

p1, p2 = 0, 0
cnt = 1 if s[0] & 1 == 1 else 0
length = 0
flag = False
while p1 < n and p2 < n:
    # print(p1, p2)
    while cnt <= k:

        p2 += 1
        try:
            if s[p2] & 1 == 1:
                # print(s[p2], p2)
                cnt += 1
        except:
            flag = True
            break

    p2 -= 1
    if not flag:
        cnt -= 1
    length = max(length, (p2 - p1 + 1 - cnt))
    # print(p1, p2, cnt)
    # print(length)
    if s[p1] & 1 == 1:
        cnt -= 1
    # print("cnt", cnt)
    p1 += 1

print(length)