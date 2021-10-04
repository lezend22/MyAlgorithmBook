# 문자열 받는 구현문제
# 머리를 먼저찾아 머리 밑 심장을 기준으로 count
# 더나은 풀이법 찾아봐
import sys

n = int(sys.stdin.readline())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

heart = (0, 0)
found = False

# 심장찾기
for i in range(n):
    if found == False:
        for j in range(n):
            if arr[i][j] == '*':
                heart = (i+1, j)
                found = True
    else:
        break

# 왼쪽, 오른쪽 팔
a, b = heart
leftArm, rightArm = 0, 0
for i in range(b):
    if arr[a][i] == '*':
        leftArm += 1
for i in range(b+1, n):
    if arr[a][i] == '*':
        rightArm += 1


# 허리
back = 0
tail = (0, 0)
for i in range(a+1, n):
    if arr[i][b] == '*':
        back += 1
        tail = (i, b)

# 왼쪽, 오른쪽 다리
c, d = tail
leftLeg, rightLeg = 0, 0
for i in range(c+1, n):
    if arr[i][d-1] == '*':
        leftLeg += 1
    if arr[i][d+1] == '*':
        rightLeg += 1

x, y = heart
print(x+1, y+1)
print(leftArm, rightArm, back, leftLeg, rightLeg)
