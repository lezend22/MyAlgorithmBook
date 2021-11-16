# 점화식만 똑바로 찾으면 바로품
# 1,000,000 이므로 한번에 d[]값 전부구한뒤
# test case별로 바로 출력
import sys

t = int(sys.stdin.readline())
d = [0] * 1000001
d[0] = 1
d[1] = 1
d[2] = 2
for i in range(3, 1000001):
    d[i] = d[i-1] % 1000000009 + d[i-2] % 1000000009 + d[i-3] % 1000000009

for _ in range(t):
    n = int(sys.stdin.readline())
    print(d[n] % 1000000009)

