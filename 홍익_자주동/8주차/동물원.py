import sys
n = int(sys.stdin.readline())
d = [0] * (n+100001)

d[1] = 3
d[2] = 7
for i in range(3, 100001):
    d[i] = (d[i-1] * 2) % 9901 + (d[i-2] % 9901)

print(d[n] % 9901)
