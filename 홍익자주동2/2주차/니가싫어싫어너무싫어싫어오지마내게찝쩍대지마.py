import sys

n = int(sys.stdin.readline())
mosq = []
maxt = 0
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if maxt < b:
        maxt = b
    mosq.append((a, b))

arr = [0] * (maxt+1)
for a, b in mosq:
    for i in range(a, b):
        if arr[i] == 0:
            arr[i] = 1

for t in range(1,)

