import heapq
import sys

n = int(sys.stdin.readline())
time = []
for i in range(n):
    s, e = map(int, sys.stdin.readline().split())
    time.append((s, e))


time.sort()
room = []
heapq.heappush(room, time[0][1])
for i in range(1, len(time)):
    a = time[i][0]
    if a >= room[0]:
        heapq.heappop(room)
        heapq.heappush(room, time[i][1])
    else:
        heapq.heappush(room, time[i][1])

print(len(room))