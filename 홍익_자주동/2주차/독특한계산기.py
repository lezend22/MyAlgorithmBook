# 왜틀린지 모르겠는문제,,
# 덱 이용해서 하나씩 계산
# 파싱하는부분 참고,, 파싱부분에서 너무 더러움
# 계산순서, type형 처리 주의
# 왜틀린거냐 내 답은 진짜 이해불가능

import sys
from collections import deque

arr = sys.stdin.readline().strip()
sign = {"*":2, "/":2, '+':1, '-':1}
num = deque()
op = deque()
p = 0

def calc(a, b, c):
    if c == '*':
        return a * b
    elif c == '/':
        return int(a / b)
    elif c == '+':
        return a + b
    elif c == '-':
        return a - b

for i in range(1, len(arr)):
    if arr[i] in {"*","/","+","-"}:
        num.append(int(arr[p:i]))
        op.append(arr[i])
        p = i+1
num.append(int(arr[p:]))

while len(num) > 1:
    front, back = op[0], op[-1]
    front, back = sign[front], sign[back]

    if front > back:
        a = num.popleft()
        b = num.popleft()
        c = op.popleft()
        calc1 = calc(a, b, c)
        num.appendleft(calc1)
    elif front < back:
        b = num.pop()
        a = num.pop()
        c = op.pop()
        calc2 = calc(a, b, c)
        num.append(calc2)
    else:
        calc1 = calc(num[0], num[1], op[0])
        calc2 = calc(num[-2], num[-1], op[-1])

        if calc1 >= calc2:
            num.popleft()
            num.popleft()
            op.popleft()
            num.appendleft(calc1)
        else:
            num.pop()
            num.pop()
            op.pop()
            num.append(calc2)
print(num[0])
