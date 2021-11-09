import sys
import math

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())

    temp = n // 2
    count = 0
    log_ = int(math.log2(n))
    print(log_+(m)+1)

