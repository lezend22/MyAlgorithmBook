import heapq
import sys
from collections import defaultdict

n = int(sys.stdin.readline())
end = []
for i in range(n):
    s, t = map(int, sys.stdin.readline().split())
    end.append((s, t))


end.sort()

room = []
heapq.heappush(room, end[0][1])

for i in range(1, len(end)):
    a = end[i][0]
    if a >= room[0]:
        heapq.heappop(room)
        heapq.heappush(room, end[i][1])
    else:
        heapq.heappush(room, end[i][1])


print(len(room))
